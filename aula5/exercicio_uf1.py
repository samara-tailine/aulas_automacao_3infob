import exercicio_f1 as funcao

funcao.imprimir("Digite um número")
n = funcao.ler()

resposta = funcao.quadrado(n)
funcao.imprimir(f"O resultado é: {resposta}")

#ou 
from exercicio_f1 import quadrado

numero = int(input("Digite um numero"))
valor = quadrado(numero)
print(f"O quadrado de {numero} é {valor}")