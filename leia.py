def leiaint():
    while True:
        try:
            n = int(input("Digite o valor: "))
        except (ValueError, TypeError):
            print("ERRO: Por favor, digite um número válido: ")
        except (KeyboardInterrupt):
            print("O usuário resolveu não digitar um número")
            return 0
        else:
            return n
    
    
def leiafloat():
    while True:
        try:
            n = float(input("Digite o valor: "))
        except (ValueError, TypeError):
            print("ERRO: Por favor, digite um número válido: ")
        except (KeyboardInterrupt):
            print("O usuário resolveu não digitar um número")
            return 0
        else:
            return n

if __name__ == '__main__':
    print(leiafloat(), leiaint())

