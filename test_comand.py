from comand import itens_validos, subtotal, desconto, fechar
from decimal import Decimal


#  Caminho normal: comanda válida com total esperado
def test_comanda_valida():
    comanda = [
        ("Banho", 50),
        ("Tosa", 80)
    ]

    resultado = fechar(comanda)

    assert resultado["subtotal"] == Decimal("130.00")
    assert resultado["desconto"] == Decimal("13.00")
    assert resultado["total"] == Decimal("117.00")


# Item fora do catálogo
def test_item_fora_catalogo():
    comanda = [
        ("Banho", 50),
        ("Brinquedo", 40)
    ]

    resultado = fechar(comanda)

    assert resultado["subtotal"] == Decimal("50.00")
    assert resultado["desconto"] == Decimal("0.00")
    assert resultado["total"] == Decimal("50.00")


#  Regra do desconto no valor exato da fronteira
def test_desconto_na_fronteira():
    comanda = [
        ("Banho", 50),
        ("Tosa", 50)
    ]

    resultado = fechar(comanda)

    assert resultado["subtotal"] == Decimal("100.00")
    assert resultado["desconto"] == Decimal("10.00")
    assert resultado["total"] == Decimal("90.00")


#  Coleção vazia
def test_comanda_vazia():
    comanda = []

    resultado = fechar(comanda)

    assert resultado["subtotal"] == Decimal("0.00")
    assert resultado["desconto"] == Decimal("0.00")
    assert resultado["total"] == Decimal("0.00")


#  Teste dos itens válidos
def test_itens_validos():
    comanda = [
        ("Banho", 50),
        ("Ração", 60),
        ("Tosa", 80)
    ]

    resultado = itens_validos(comanda)

    assert resultado == [
        ("Banho", 50),
        ("Tosa", 80)
    ]