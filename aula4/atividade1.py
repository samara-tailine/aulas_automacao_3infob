while True: 
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    if (usuario == 'admin' and senha == 'admin123'):
        print("Bem-vindo")
        break
    else:
        print("Usuário ou senha inválido")


#ou

usuario = ''
senha = ''

while (usuario != 'admin' or senha != 'admin123'):
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

print("Bem-vindo")

#while not (== and ==)
#while (!= or !=)
 

