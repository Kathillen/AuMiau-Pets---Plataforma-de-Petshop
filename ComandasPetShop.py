class Servicos:
    def __init__(self, servico, preco):
        self.servico = servico
        self._preco = preco
        
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = valor

    def calcular_total(self, quantidade):
        return self.preco * quantidade
    
servico_solicitado1 = Servicos("Tosa", 50)
servico_solicitado2 = Servicos("Banho", 70)


print("Servicos solicitados por cliente:")

print(servico_solicitado1.servico)
print(servico_solicitado1._preco)

print(servico_solicitado2.servico)
print(servico_solicitado2._preco)

print("---------------------------------")


print("Servicos solicitados por cliente total do valor :")


print(servico_solicitado1.servico)
print(servico_solicitado1.calcular_total(2))

print(servico_solicitado2.servico)
print(servico_solicitado2.calcular_total(3))

print("---------------------------------")


