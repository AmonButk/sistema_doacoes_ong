from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:
    def __init__(self):
        # Nomes dos 5 integrantes do grupo definidos no planejamento (Seção 6)
        self.created_by = (
            "Amon",
            "Gabriel",
            "Maria Vitória",
            "Pedro Paulo",
            "Ricardo"
        )
        self.professor = "Prof. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2026/2"

    def get_total_doadores(self) -> int:
        """
        Consulta o banco de dados e retorna o total de registros na tabela DOADORES.
        Utiliza config.QUERY_COUNT formatando a tabela correspondente.
        """
        oracle = OracleQueries()
        oracle.connect()
        query = config.QUERY_COUNT.format(tabela="doadores")
        df = oracle.sqlToDataFrame(query)
        # A coluna retornada em minúsculo pelo OracleQueries é 'total_doadores'
        return int(df["total_doadores"].values[0])

    def get_total_doacoes(self) -> int:
        """
        Consulta o banco de dados e retorna o total de registros na tabela DOACOES.
        Utiliza config.QUERY_COUNT formatando a tabela correspondente.
        """
        oracle = OracleQueries()
        oracle.connect()
        query = config.QUERY_COUNT.format(tabela="doacoes")
        df = oracle.sqlToDataFrame(query)
        # A coluna retornada em minúsculo pelo OracleQueries é 'total_doacoes'
        return int(df["total_doacoes"].values[0])

    def get_updated_screen(self) -> str:
        """
        Monta e retorna a tela de abertura (Splash Screen) com contagens atualizadas
        e identificação do sistema, integrantes, professor e semestre.
        """
        total_doadores = self.get_total_doadores()
        total_doacoes = self.get_total_doacoes()

        integrantes_str = ", ".join(self.created_by)

        return f"""
        ########################################################
        #             SISTEMA DE DOAÇÕES PARA ONG              #
        #                                                      #
        # TOTAL DE REGISTROS:                                  #
        #   1 - DOADORES: {str(total_doadores).rjust(5)}                                #
        #   2 - DOAÇÕES:  {str(total_doacoes).rjust(5)}                                #
        #                                                      #
        # CRIADO POR: {integrantes_str}
        # PROFESSOR:  {self.professor}
        # DISCIPLINA: {self.disciplina}
        # SEMESTRE:   {self.semestre}
        ########################################################
        """

