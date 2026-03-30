while True: 
    try:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))

        divisão = n1 / n2

        print("Resultado da divisão:", divisão)
        break
    except ValueError:
        print("O valor digitado é inválido")
    except ZeroDivisionError:
        print("Você não pode dividir por zero")
    except Exception as e:
        print("Ocorreu um erro", e)
