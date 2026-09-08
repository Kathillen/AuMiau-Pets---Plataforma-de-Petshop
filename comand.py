from decimal import Decimal

catalogo = {
    "Banho": Decimal("50.00"),
    "Tosa": Decimal("80.00"),
    "Corte de unhas": Decimal("20.00"),
    "Higienização dos dentes": Decimal("30.00")
}


def itens_validos(comanda):
    itens = []

    for item, preco in comanda:
        if item not in catalogo:
            continue

        itens.append((item, preco))

    return itens


def subtotal(comanda):
    total = Decimal("0.00")

    for item, preco in itens_validos(comanda):
        total += Decimal(str(preco))

    return total


def desconto(comanda, valor):
    sub = subtotal(comanda)

    if sub >= Decimal("100.00"):
        return sub * Decimal("0.10")

    return Decimal("0.00")


def fechar(comanda):
    sub = subtotal(comanda)
    desc = desconto(comanda, sub)
    total = sub - desc

    return {
        "subtotal": sub,
        "desconto": desc,
        "total": total
    }


# Comanda
comanda = [
    ("Banho", 50),
    ("Tosa", 80),
    ("Brinquedo", 40),
    ("Ração", 60)
]


resultado = fechar(comanda)

print(f"Subtotal: R$ {resultado['subtotal']:.2f}")
print(f"Desconto: R$ {resultado['desconto']:.2f}")
print(f"Total: R$ {resultado['total']:.2f}")