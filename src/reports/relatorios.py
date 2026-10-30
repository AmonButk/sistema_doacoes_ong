from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        # Abre e armazena o conteúdo das consultas SQL a partir da pasta sql/
        # Observação: a execução ocorre a partir da pasta src/
        with open("sql/relatorio_arrecadacao_por_campanha.sql", "r", encoding="utf-8") as f:
            self.query_relatorio_arrecadacao = f.read()

        with open("sql/relatorio_doacoes.sql", "r", encoding="utf-8") as f:
            self.query_relatorio_doacoes = f.read()

        with open("sql/relatorio_doadores.sql", "r", encoding="utf-8") as f:
            self.query_relatorio_doadores = f.read()

    def get_relatorio_arrecadacao_por_campanha(self):
        """
        Executa a consulta de sumarização e exibe o total arrecadado por campanha.
        """
        oracle = OracleQueries()
        oracle.connect()
        df = oracle.sqlToDataFrame(self.query_relatorio_arrecadacao)
        print("\n" + "=" * 60)
        print("RELATÓRIO: ARRECADAÇÃO POR CAMPANHA")
        print("=" * 60)
        print(df)
        print("=" * 60 + "\n")
        input("Pressione Enter para sair do relatório")

    def get_relatorio_doacoes(self):
        """
        Executa a consulta de junção e exibe os dados detalhados das doações.
        """
        oracle = OracleQueries()
        oracle.connect()
        df = oracle.sqlToDataFrame(self.query_relatorio_doacoes)
        print("\n" + "=" * 60)
        print("RELATÓRIO: DOAÇÕES DETALHADAS")
        print("=" * 60)
        print(df)
        print("=" * 60 + "\n")
        input("Pressione Enter para sair do relatório")

    def get_relatorio_doadores(self):
        """
        Executa a consulta e exibe a listagem completa dos doadores cadastrados.
        """
        oracle = OracleQueries()
        oracle.connect()
        df = oracle.sqlToDataFrame(self.query_relatorio_doadores)
        print("\n" + "=" * 60)
        print("RELATÓRIO: LISTAGEM DE DOADORES")
        print("=" * 60)
        print(df)
        print("=" * 60 + "\n")
        input("Pressione Enter para sair do relatório")

