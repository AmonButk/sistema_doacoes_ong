#Responsavel: Gabriel Ridolfi
#classe que representa um doador, com seus atributos e metodos de acesso

class Doador:
    def __init__(self,
                 cpf:str=None,
                 nome:str=None,
                 email:str=None,
                 telefone:str=None
                ):

        self.set_cpf(cpf)
        self.set_nome(nome)
        self.set_email(email)
        self.set_telefone(telefone)

    def set_cpf(self, cpf:str):
        self.cpf = cpf

    def set_nome(self, nome:str):
        self.nome = nome

    def set_email(self, email:str):
        self.email = email

    def set_telefone(self, telefone:str):
        self.telefone = telefone

    def get_cpf(self) -> str:
        return self.cpf

    def get_nome(self) -> str:
        return self.nome

    def get_email(self) -> str:
        return self.email

    def get_telefone(self) -> str:
        return self.telefone

    def to_string(self) -> str:
        #email e telefone podem ser none, substituí por "-" para ficar mais legivel
        email = self.get_email() if self.get_email() else "-"
        telefone = self.get_telefone() if self.get_telefone() else "-"
        return f"CPF: {self.get_cpf()} | Nome: {self.get_nome()} | Email: {email} | Telefone: {telefone}"
