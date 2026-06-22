#1) Importar a biblioteca pandas
import pandas as pd

#2) Carregar uma planilha do Excel:
#Lê o arquivo que está no caminho e armazena na variável  df
df = pd.read_excel('revisao\\planilha.xlsx')
print(df.head())

#3) Compreender o funcionamneto do loc
print(df.loc[0]) #imprime a 1º linha
print(df.loc [0, "Nome"]) #imprime a coluna Nome da 1º linha [linha, coluna]
print(df.loc[4 : 6]) #[linha inicial : linha final] ou seleciona o intervalo de linhas entre 4 e 6
print(df.loc[4 : 6, "Nome"]) #seleciona a coluna Nome das linhas entre 4 e 6
print(df.loc[4 : 6, ["Nome", "Idade"]]) #seleciona as colunas Nome e Idade das linhas 4, 5 e 6
print(df.loc[ : , "Nome"]) #localizar uma única coluna - todas as linhas

df2 = df.loc[3:6, ["Nome", "Sexo"]] 
print(df2)

print(df2.loc[[True, False, False, True], ["Nome", "Sexo"]]) 

#4) Inserir novos dados na planilha
df.loc[len(df)] = ["Isis", "Feminino", 18, "Técnico em Informática", "Automação T", 10] 
print(df)

#5) Atualizar dados na planilha
df.loc[30, ["Curso", "Disciplina"]] = ["Artes", "Teatro"]
print(df)

#6) Filtrar dados
condicao1 = df["Idade"] == 20
condicao2 = df["Sexo"] == 'Feminino'
print(df.loc[condicao1 & condicao2, 'Nome']) #com ou sem a coluna

#7) Classificar dados
tabela_ordenada = df.sort_values('Nome') #ascending=False -> inverte a ordem da planinha Z-A
print(tabela_ordenada)

#8) Contar dados
contagem = df.value_counts('Curso')
print(contagem)

#9) Agrupar dados
tabela_agrupada = df.groupby('Disciplina')['Nota'].mean() #mean: média, sum: soma, count: conta
print(tabela_agrupada)

#10) Exportar dados
df.to_excel('revisao\\nova_planilha.xlsx')