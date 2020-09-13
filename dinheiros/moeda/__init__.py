

def aumentar(valor, aumento, beleza=False):
    if beleza == True:
        return moeda(valor + valor * aumento / 100)
    return valor + valor * aumento / 100

def reduzir(valor, reducao, beleza=False):
    if beleza == True:
        return moeda(valor - valor * reducao / 100)
    return valor - valor * reducao / 100

def dobro(valor, beleza=False):
    if beleza == True:
        return moeda(valor * 2)
    return valor * 2

def metade(valor, beleza=False):
    if beleza == True:
        return moeda(valor / 2)
    return valor / 2

def moeda(valor):
    return f"R${valor:.2f}".replace(".", ",")


def resumo(valor, aumento, reducao):
    print("-"*30 + "\n"
    "RESUMO DO VALOR \n" + "-"*30 + "\n"
    f"Preco analisado:{moeda(valor)} \n"
    f"Dobro do preco:{dobro(valor, True)} \n" 
    f"Metade do preco:{metade(valor, True)} \n" 
    f"{aumento}% de aumento:{aumentar(valor, aumento, True)} \n"
    f"{reducao}% de reducao:{reduzir(valor, reducao, True)} \n" + "-"*30)
    


