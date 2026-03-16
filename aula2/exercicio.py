n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media >= 6:
    print("Aprovado")
else:
    ef = float(input(("Digite a nota do exame final: ")))
    media2 = (media + ef) / 2
    if media2 > 6:
        print("Aprovado")
    else: 
        print("Reprovado")
