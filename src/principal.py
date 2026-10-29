from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_doador import Controller_Doador
from controller.controller_doacao import Controller_Doacao

# Objetos usados pelo menu (criados uma vez só)
tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_doador = Controller_Doador()
ctrl_doacao = Controller_Doacao()


def reports(opcao_relatorio: int = 0):
    if opcao_relatorio == 1:
        relatorio.get_relatorio_arrecadacao_por_campanha()
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_doacoes()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_doadores()
    elif opcao_relatorio == 0:
        return
    else:
        print("Opção de relatório inválida!")


def inserir(opcao_inserir: int = 0):
    if opcao_inserir == 1:
        ctrl_doador.inserir_doador()
    elif opcao_inserir == 2:
        ctrl_doacao.inserir_doacao()
    elif opcao_inserir == 0:
        return
    else:
        print("Opção inválida!")


def atualizar(opcao_atualizar: int = 0):
    if opcao_atualizar == 1:
        ctrl_doador.atualizar_doador()
    elif opcao_atualizar == 2:
        ctrl_doacao.atualizar_doacao()
    elif opcao_atualizar == 0:
        return
    else:
        print("Opção inválida!")


def excluir(opcao_excluir: int = 0):
    if opcao_excluir == 1:
        ctrl_doador.excluir_doador()
    elif opcao_excluir == 2:
        ctrl_doacao.excluir_doacao()
    elif opcao_excluir == 0:
        return
    else:
        print("Opção inválida!")


def ler_inteiro(mensagem: str) -> int:
    # Repete a pergunta até o usuário digitar um número (evita o programa fechar com ValueError)
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite apenas o número da opção.")


def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = ler_inteiro("Escolha uma opção [1-5]: ")
        config.clear_console(1)

        if opcao == 1:  # Relatórios
            while True:
                print(config.MENU_RELATORIOS)
                opcao_relatorio = ler_inteiro("Escolha uma opção [0-3]: ")
                config.clear_console(1)

                if opcao_relatorio == 0:
                    break

                reports(opcao_relatorio)
                config.clear_console(1)

        elif opcao == 2:  # Inserir Novos Registros
            print(config.MENU_ENTIDADES)
            opcao_inserir = ler_inteiro("Escolha uma opção [0-2]: ")
            config.clear_console(1)

            if opcao_inserir != 0:
                inserir(opcao_inserir=opcao_inserir)
                config.clear_console()
                print(tela_inicial.get_updated_screen())
                config.clear_console()

        elif opcao == 3:  # Atualizar Registros
            print(config.MENU_ENTIDADES)
            opcao_atualizar = ler_inteiro("Escolha uma opção [0-2]: ")
            config.clear_console(1)

            if opcao_atualizar != 0:
                atualizar(opcao_atualizar=opcao_atualizar)
                config.clear_console()

        elif opcao == 4:  # Remover Registros
            print(config.MENU_ENTIDADES)
            opcao_excluir = ler_inteiro("Escolha uma opção [0-2]: ")
            config.clear_console(1)

            if opcao_excluir != 0:
                excluir(opcao_excluir=opcao_excluir)
                config.clear_console()
                print(tela_inicial.get_updated_screen())
                config.clear_console()

        elif opcao == 5:  # Sair
            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o Sistema de Doações para ONG!")
            exit(0)

        else:
            print("Opção incorreta! Escolha um número entre 1 e 5.")
            config.clear_console(1)


if __name__ == "__main__":
    run()
