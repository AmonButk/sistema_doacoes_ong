import os
import time

MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Arrecadação por Campanha
2 - Doações Detalhadas
3 - Doadores
0 - Voltar
"""

MENU_ENTIDADES = """Entidades
1 - DOADORES
2 - DOAÇÕES
0 - Voltar
"""

# Query padronizada para contagem de registros (Requisito 5c do edital)
QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time: int = 3):
    """
    Aguarda wait_time segundos e limpa a tela do terminal.
    Compatível com Windows e Linux.
    """
    time.sleep(wait_time)
    os.system("cls" if os.name == "nt" else "clear")

