
from decimal import Decimal


class Servicos:
    def __init__(self, servico, preco):
        self.servico = servico
        self._preco = Decimal(str(preco))

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        valor = Decimal(str(valor))

        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")

        self._preco = valor

    def calcular_total(self, quantidade, peso):
        if peso == 9:
            total = self.preco + Decimal("10.00")
        elif peso >= 10:
            total = self.preco + Decimal("15.00")
        else:
            total = self.preco
        return total * quantidade


# Catálogo de serviços e preços
catalogo = {
    "Banho": Decimal("50.00"),
    "Tosa": Decimal("80.00"),
    "Corte de unhas": Decimal("20.00"),
    "Higienização dos dentes": Decimal("30.00")
}


# O usuário informa o serviço e a quantidade
nome = input("Digite o nome do serviço: ").strip().title()

if nome in catalogo:
    quantidade = int(input("Digite a quantidade: "))
    kgAnimal = float(input("Qual é o peso do animal?"))

    servico_solicitado = Servicos(nome, catalogo[nome])

    total = servico_solicitado.calcular_total(quantidade, kgAnimal)

    print("\nServiço solicitado:")
    print(f"Nome: {servico_solicitado.servico}")
    print(f"Preço unitário: R$ {servico_solicitado.preco:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Total: R$ {total:.2f}")

else:
    print("Serviço não encontrado no catálogo.")
