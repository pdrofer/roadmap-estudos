class Pedido:
    def __init__(self, itens):
        self.itens = itens

    def calcular_total(self):
        return sum(item["preco"] for item in self.itens)


class NotificadorEmail:
    def enviar_confirmacao(self, email):
        print(f"Enviando email de confirmação para {email}")
