def leiadinheiro():
    valor = input("Digite o valor: ").replace(",", ".")
    while True:
        try:
            float(valor)
            break
        except ValueError:
            print("Numero invalido")
            return leiadinheiro()
    return float(valor)
    


    
print(leiadinheiro())