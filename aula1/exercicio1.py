salario = input("Digite seu salário: ")
inss = int(salario) * (11/100)
fgts = int(salario) * (7.5/100)
sf = int(salario) - inss - fgts

print("Seu salário líquido é:", sf)
print("Desconto INSS:", inss)
print("Desconto FGTS:", fgts)