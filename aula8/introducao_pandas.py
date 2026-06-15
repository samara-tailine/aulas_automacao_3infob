import pandas as pd 

#ler a planilha do Excel utilizando pandas
planilha = pd.read_excel('aula8\\Alunos.xlsx') 

#imprime a variável planilha
print(planilha)

#imprime os dados da aluna Gabriela, imprime a linha 12
print(planilha.loc[12])

#imprime o nome da aluna Gabriela, imprime a linha 12
print(planilha.loc[12, "Nome"])

#imprime o nome e idade da aluna Gabriela, imprime a linha 12
print(planilha.loc[12, ["Nome", "Idade"]])

#atualizar os dados da Gabriela
planilha.loc[12, "Nome"] = "Gabriela Pereira"
planilha.loc[12, ["Nome", "Idade"]] = ["Gabriela Pereira de Souza", 20]

#inserir dados na planilha
planilha.loc[len(planilha), ["Nome", "Idade"]] = ['Ivan', 40]

print(planilha)
