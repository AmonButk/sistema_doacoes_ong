# -*- coding: utf-8 -*-
'''
controller_doacao.py
Responsável: Maria Vitória

Controller da entidade DOACOES (Sistema de Doações para ONG): inserção,
atualização e exclusão de doações, além da listagem, verificação de
existência e recuperação de uma doação pelo ID.

Segue o contrato técnico da seção 5.1 do plano: cada operação abre a própria
conexão, faz os input() internamente, termina com o laço "(S/N)" e monta o SQL
em string, sem ORM.
'''
from datetime import date, datetime

from model.doacoes import Doacao
from model.doadores import Doador
from controller.controller_doador import Controller_Doador
from conexion.oracle_queries import OracleQueries

VALOR_MAXIMO_DOACAO = 99999999.99  # limite de NUMBER(10,2)
TAMANHO_MAXIMO_CAMPANHA = 60       # limite de VARCHAR2(60)


class Controller_Doacao:
    '''Operações de CRUD da tabela DOACOES, interagindo com o usuário via terminal.'''

    def __init__(self):
        # Toda doação pertence a um doador (FK CPF); reaproveitamos o controller
        # de doadores para listar/validar sem duplicar SQL.
        self.ctrl_doador = Controller_Doador()

    def inserir_doacao(self) -> Doacao:
        '''
        Cadastra novas doações até o usuário responder "N".
        O ID é gerado pela sequence DOACOES_ID_DOACAO_SEQ dentro de um bloco
        PL/SQL anônimo, que devolve o valor por uma variável de saída (bind).
        Retorna a última doação inserida, ou None se nenhuma foi gravada.

        Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks
        '''
        ultima_doacao_inserida = None

        while True:
            oracle = OracleQueries(can_write=True)
            oracle.connect()

            self.ctrl_doador.listar_doadores(oracle)
            cpf_informado = input("Digite o CPF do Doador: ").strip()
            doador = self.valida_doador(oracle, cpf_informado)

            if doador is not None:
                campanha = self.ler_campanha()
                valor = self.ler_valor()
                data_doacao = self.ler_data()

                cursor = oracle.cur
                id_gerado = cursor.var(int)

                cursor.execute("""
                begin
                    :id_doacao := DOACOES_ID_DOACAO_SEQ.NEXTVAL;
                    insert into doacoes (id_doacao, cpf, campanha, valor, data_doacao)
                    values (:id_doacao, :cpf, :campanha, :valor, :data_doacao);
                end;
                """, dict(id_doacao=id_gerado,
                          cpf=doador.get_cpf(),
                          campanha=campanha,
                          valor=valor,
                          data_doacao=data_doacao))

                id_doacao = int(id_gerado.getvalue())
                oracle.conn.commit()

                ultima_doacao_inserida = self.get_doacao_from_id(oracle, id_doacao)
                print("\nDoação inserida com sucesso!")
                print(ultima_doacao_inserida.to_string())

            if not self.pergunta_sim_nao("\nDeseja inserir mais algum registro? (S/N): "):
                break

        return ultima_doacao_inserida

    def atualizar_doacao(self) -> Doacao:
        '''
        Altera todos os atributos de uma doação existente, exceto o ID (PK),
        repetindo até o usuário responder "N". Após o UPDATE, o registro é
        relido do banco para exibir exatamente o que foi persistido.
        Retorna a última doação atualizada, ou None se nenhuma foi alterada.
        '''
        ultima_doacao_atualizada = None

        while True:
            oracle = OracleQueries(can_write=True)
            oracle.connect()

            self.listar_doacoes(oracle)
            id_doacao = self.ler_id("ID da Doação que deseja alterar: ")

            if id_doacao is not None and self.verifica_existencia_doacao(oracle, id_doacao):
                self.ctrl_doador.listar_doadores(oracle)
                cpf_informado = input("Digite o CPF do Doador (Novo): ").strip()
                doador = self.valida_doador(oracle, cpf_informado)

                if doador is not None:
                    campanha = self.ler_campanha()
                    valor = self.ler_valor()
                    data_doacao = self.ler_data()

                    # Aspas simples são duplicadas para não fechar a string SQL
                    # antes da hora (ex.: "Natal D'Ouro").
                    campanha_escapada = campanha.replace("'", "''")
                    oracle.write(f"update doacoes "
                                 f"set cpf = '{doador.get_cpf()}', "
                                 f"campanha = '{campanha_escapada}', "
                                 f"valor = {valor:.2f}, "
                                 f"data_doacao = to_date('{data_doacao.strftime('%d/%m/%Y')}', 'DD/MM/YYYY') "
                                 f"where id_doacao = {id_doacao}")

                    ultima_doacao_atualizada = self.get_doacao_from_id(oracle, id_doacao)
                    print("\nDoação atualizada com sucesso!")
                    print(ultima_doacao_atualizada.to_string())
            elif id_doacao is not None:
                print(f"A doação de ID {id_doacao} não existe.")

            if not self.pergunta_sim_nao("\nDeseja atualizar mais algum registro? (S/N): "):
                break

        return ultima_doacao_atualizada

    def listar_doacoes(self, oracle:OracleQueries, need_connect:bool=False) -> None:
        '''
        Exibe as doações cadastradas com o nome do doador (JOIN com DOADORES),
        para o usuário identificar o registro sem precisar decorar CPFs.
        need_connect=True abre a conexão quando o chamador ainda não o fez.
        '''
        query = """
                select d.id_doacao
                     , dd.nome
                     , d.campanha
                     , d.valor
                  from doacoes d
                 inner join doadores dd
                    on d.cpf = dd.cpf
                 order by d.id_doacao
                """
        if need_connect:
            oracle.connect()
        df_doacoes = oracle.sqlToDataFrame(query)
        if df_doacoes.empty:
            print("Nenhuma doação cadastrada.")
        else:
            print(df_doacoes.to_string(index=False))

    def verifica_existencia_doacao(self, oracle:OracleQueries, id_doacao:int=None) -> bool:
        '''Retorna True se a doação EXISTE (lógica inversa à do projeto de exemplo, conforme o contrato).'''
        df_doacao = oracle.sqlToDataFrame(f"select id_doacao from doacoes where id_doacao = {id_doacao}")
        return not df_doacao.empty

    def get_doacao_from_id(self, oracle:OracleQueries, id_doacao:int=None) -> Doacao:
        '''
        Monta o objeto Doacao, com o objeto Doador completo dentro, a partir do ID.
        Retorna None se o ID não existir.
        '''
        df_doacao = oracle.sqlToDataFrame(f"select id_doacao, cpf, campanha, valor, data_doacao "
                                          f"from doacoes where id_doacao = {id_doacao}")
        if df_doacao.empty:
            return None
        linha_doacao = df_doacao.iloc[0]
        cpf_doador = str(linha_doacao["cpf"])

        # A FK garante que o doador existe; o fallback evita que to_string()
        # quebre caso get_doador_from_cpf retorne None por algum motivo.
        doador = self.ctrl_doador.get_doador_from_cpf(oracle, cpf_doador)
        if doador is None:
            doador = Doador(cpf=cpf_doador, nome="(doador não encontrado)")

        return Doacao(int(linha_doacao["id_doacao"]),
                      doador,
                      str(linha_doacao["campanha"]),
                      float(linha_doacao["valor"]),
                      self.converte_data(linha_doacao["data_doacao"]))

    def valida_doador(self, oracle:OracleQueries, cpf:str=None) -> Doador:
        '''
        Retorna o Doador do CPF informado, ou None (com aviso) se não existir.
        A segunda checagem cobre o caso de get_doador_from_cpf retornar None.
        '''
        doador = None
        if self.ctrl_doador.verifica_existencia_doador(oracle, cpf):
            doador = self.ctrl_doador.get_doador_from_cpf(oracle, cpf)
        if doador is None:
            print(f"O CPF {cpf} informado não existe na base. A doação não foi gravada.")
        return doador

    def ler_id(self, mensagem:str) -> int:
        '''Lê um ID numérico; retorna None em entrada inválida, sem derrubar o programa.'''
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("ID inválido. Digite apenas números.")
            return None

    def ler_campanha(self) -> str:
        '''Lê o nome da campanha respeitando as restrições da coluna (NOT NULL, VARCHAR2(60)).'''
        while True:
            campanha = input("Campanha: ").strip()
            if campanha == "":
                print("A campanha não pode ficar em branco.")
            elif len(campanha) > TAMANHO_MAXIMO_CAMPANHA:
                print(f"A campanha pode ter no máximo {TAMANHO_MAXIMO_CAMPANHA} caracteres.")
            else:
                return campanha

    def ler_valor(self) -> float:
        '''
        Lê o valor da doação aceitando vírgula ou ponto como separador decimal.
        Valida antes do banco o CHECK (valor > 0) e o limite de NUMBER(10,2).
        '''
        while True:
            valor_digitado = input("Valor (R$): ").strip().replace(",", ".")
            try:
                valor = round(float(valor_digitado), 2)
            except ValueError:
                print("Valor inválido. Exemplo: 50,00 ou 50.00")
                continue
            if valor <= 0:
                print("O valor deve ser maior que zero.")
            elif valor > VALOR_MAXIMO_DOACAO:
                print("Valor muito alto. O máximo é 99999999,99.")
            else:
                return valor

    def ler_data(self) -> date:
        '''Lê a data no formato DD/MM/AAAA e a converte para date.'''
        while True:
            data_digitada = input("Data da doação (DD/MM/AAAA): ").strip()
            try:
                return datetime.strptime(data_digitada, "%d/%m/%Y").date()
            except ValueError:
                print("Data inválida. Use o formato DD/MM/AAAA, ex.: 27/10/2026")

    def pergunta_sim_nao(self, mensagem:str) -> bool:
        '''Repete a pergunta até obter S/SIM (True) ou N/NAO/NÃO (False).'''
        while True:
            resposta = input(mensagem).strip().upper()
            if resposta in ("S", "SIM"):
                return True
            if resposta in ("N", "NAO", "NÃO"):
                return False
            print("Resposta inválida. Digite S ou N.")

    def converte_data(self, data_do_banco) -> date:
        '''O pandas devolve DATE do Oracle como Timestamp; o model espera datetime.date.'''
        if hasattr(data_do_banco, "date"):
            return data_do_banco.date()
        return data_do_banco
