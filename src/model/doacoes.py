#classe de modelo Doacao.
from datetime import date
from model.doadores import Doador

class Doacao:
    def __init__(self,
                 id_doacao:int=None,
                 doador:Doador=None,
                 campanha:str=None,
                 valor:float=None,
                 data_doacao:date=None
                ):
        self.set_id_doacao(id_doacao)
        self.set_doador(doador)
        self.set_campanha(campanha)
        self.set_valor(valor)
        self.set_data_doacao(data_doacao)

    def set_id_doacao(self, id_doacao:int):
        self.id_doacao = id_doacao

    def set_doador(self, doador:Doador):
        self.doador = doador

    def set_campanha(self, campanha:str):
        self.campanha = campanha

    def set_valor(self, valor:float):
        self.valor = valor

    def set_data_doacao(self, data_doacao:date):
        self.data_doacao = data_doacao

    def get_id_doacao(self) -> int:
        return self.id_doacao

    def get_doador(self) -> Doador:
        return self.doador

    def get_campanha(self) -> str:
        return self.campanha

    def get_valor(self) -> float:
        return self.valor

    def get_data_doacao(self) -> date:
        return self.data_doacao

    # Métodos criados para formatar os valores de exibição de dinheiro e data
    def _formata_valor(self) -> str:
        if self.get_valor() is None:
            return "-"
        texto = f"{float(self.get_valor()):,.2f}" 
        return texto.replace(",", "X").replace(".", ",").replace("X", ".")

    def _formata_data(self) -> str:
        data = self.get_data_doacao()
        if data is None:
            return "-"
        try:
            from pandas import Timestamp
            return Timestamp(data).strftime("%d/%m/%Y")
        except Exception:
            return str(data)

    def to_string(self) -> str:
        nome_doador = self.get_doador().get_nome() if self.get_doador() else "-"
        return (f"Doação: {self.get_id_doacao()} | Doador: {nome_doador} | "
                f"Campanha: {self.get_campanha()} | Valor: R$ {self._formata_valor()} | "
                f"Data: {self._formata_data()}")
