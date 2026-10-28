from model.doadores import Doador
from conexion.oracle_queries import OracleQueries

class Controller_Doador:
    def __init__(self):
        pass

    def inserir_doador(self) -> Doador:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        ultimo_doador = None 
        while True:
            # cpf com 11 digitos
            cpf = self._ler_cpf("CPF do doador (Novo, somente números): ")

            if self.verifica_existencia_doador(oracle, cpf):
                print(f"O CPF {cpf} já está cadastrado. Nenhum registro foi inserido.")
            else:
                nome = self._ler_texto("Nome (Novo): ", tamanho_max=100, obrigatorio=True)
                email = self._ler_texto("Email (Novo, Enter para deixar em branco): ", tamanho_max=100)
                telefone = self._ler_texto("Telefone (Novo, Enter para deixar em branco): ", tamanho_max=15)

                oracle.write(f"insert into doadores (cpf, nome, email, telefone) "
                             f"values ('{cpf}', {self._sql_texto(nome)}, "
                             f"{self._sql_texto(email)}, {self._sql_texto(telefone)})")

                ultimo_doador = self.get_doador_from_cpf(oracle, cpf)
                print("Doador inserido com sucesso!")
                print(ultimo_doador.to_string())

            if not self._confirma("Deseja inserir mais algum registro? (S/N): "):
                break

        return ultimo_doador

    def atualizar_doador(self) -> Doador:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        ultimo_doador = None
        while True:
            self.listar_doadores(oracle)
            cpf = self._ler_cpf("CPF do doador que deseja alterar: ")

            if not self.verifica_existencia_doador(oracle, cpf):
                print(f"O CPF {cpf} não existe.")
            else:
                print("Registro atual:")
                print(self.get_doador_from_cpf(oracle, cpf).to_string())

                novo_nome = self._ler_texto("Nome (Novo): ", tamanho_max=100, obrigatorio=True)
                novo_email = self._ler_texto("Email (Novo, Enter para deixar em branco): ", tamanho_max=100)
                novo_telefone = self._ler_texto("Telefone (Novo, Enter para deixar em branco): ", tamanho_max=15)

                oracle.write(f"update doadores set "
                             f"nome = {self._sql_texto(novo_nome)}, "
                             f"email = {self._sql_texto(novo_email)}, "
                             f"telefone = {self._sql_texto(novo_telefone)} "
                             f"where cpf = '{cpf}'")

                ultimo_doador = self.get_doador_from_cpf(oracle, cpf)
                print("Doador atualizado com sucesso!")
                print(ultimo_doador.to_string())

            if not self._confirma("Deseja atualizar mais algum registro? (S/N): "):
                break

        return ultimo_doador

    def excluir_doador(self) -> None:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        while True:
            self.listar_doadores(oracle)
            cpf = self._ler_cpf("CPF do doador que deseja excluir: ")

            if not self.verifica_existencia_doador(oracle, cpf):
                print(f"O CPF {cpf} não existe.")
            else:
                doador = self.get_doador_from_cpf(oracle, cpf)
                print(doador.to_string())

                if not self._confirma("Confirma a exclusão? (S/N): "):
                    print("Exclusão cancelada.")
                else:
                    df_qtd = oracle.sqlToDataFrame(
                        f"select count(1) as qtd from doacoes where cpf = '{cpf}'")
                    qtd_doacoes = int(df_qtd.qtd.values[0])

                    if qtd_doacoes > 0:
                        print(f"Este doador possui {qtd_doacoes} doações.")
                        if self._confirma("Deseja excluir também as doações dele? (S/N): "):
                            
                            oracle.write(f"delete from doacoes where cpf = '{cpf}'")
                            print(f"{qtd_doacoes} doação(ões) removida(s) com sucesso!")
                            
                            oracle.write(f"delete from doadores where cpf = '{cpf}'")
                            print("Doador removido com sucesso!")
                            print(doador.to_string())
                        else:
                            print("Exclusão cancelada. O doador e suas doações foram mantidos.")
                    else:
                        oracle.write(f"delete from doadores where cpf = '{cpf}'")
                        print("Doador removido com sucesso!")
                        print(doador.to_string())

            if not self._confirma("Deseja excluir mais algum registro? (S/N): "):
                break

    # metodos de apoio que o controller_doacao tambem usa
    def listar_doadores(self, oracle:OracleQueries, need_connect:bool=False) -> None:
        query = """
                select d.cpf
                     , d.nome
                  from doadores d
                 order by d.nome
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def verifica_existencia_doador(self, oracle:OracleQueries, cpf:str) -> bool:
        df_doador = oracle.sqlToDataFrame(f"select cpf from doadores where cpf = '{cpf}'")
        return not df_doador.empty

    def get_doador_from_cpf(self, oracle:OracleQueries, cpf:str) -> Doador:
        df_doador = oracle.sqlToDataFrame(
            f"select cpf, nome, email, telefone from doadores where cpf = '{cpf}'")
        if df_doador.empty:
            return None
        return Doador(df_doador.cpf.values[0],
                      df_doador.nome.values[0],
                      df_doador.email.values[0],
                      df_doador.telefone.values[0])

    def _ler_cpf(self, mensagem:str) -> str:
        while True:
            cpf = "".join(c for c in input(mensagem) if c.isdigit())
            if len(cpf) == 11:
                return cpf
            print("CPF inválido. Digite os 11 números do CPF.")

    def _ler_texto(self, mensagem:str, tamanho_max:int, obrigatorio:bool=False) -> str:
        while True:
            texto = input(mensagem).strip()
            if obrigatorio and texto == "":
                print("Este campo é obrigatório.")
            elif len(texto) > tamanho_max:
                print(f"Máximo de {tamanho_max} caracteres.")
            else:
                return texto

    def _sql_texto(self, valor:str) -> str:
        if valor is None or valor == "":
            return "null"
        return "'" + valor.replace("'", "''") + "'"

    def _confirma(self, mensagem:str) -> bool:
        while True:
            resposta = input(mensagem).strip().upper()
            if resposta in ("S", "N"):
                return resposta == "S"
            print("Resposta inválida. Digite S ou N.")
