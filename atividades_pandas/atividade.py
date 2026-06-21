import pandas as pd

#1 Leitura de Dados
df_notas = pd.read_excel("atividades_pandas\\notas_estudantes.xlsx", sheet_name="Notas")
df_atividades = pd.read_excel("atividades_pandas\\notas_estudantes.xlsx", sheet_name="Atividades")
print(df_notas)
print(df_atividades)

#2 Inserção de Registro
df_notas.loc[len(df_notas)] = ['Lucas Silva', 'Prova Final', 8.5]
print(df_notas)

#3 Atualização de Dados
df_notas.loc[(df_notas['Nome'] == "Ana Souza") & (df_notas['Atividade'] == "Trabalho 1"), "Nota"] = 9
print(df_notas)

#4 Exclusão de Registro
df_notas.drop(df_notas.loc[(df_notas['Nome'] == "Pedro Santos") & (df_notas['Atividade'] == "Prova 1"), "Nota"].index, inplace=True)
print(df_notas)

#5  Filtragem Simples
resposta = df_notas.loc[df_notas['Nota'] > 7]
print(resposta)

#6 Agrupamento e Agregação
resposta = df_notas.groupby('Nome')['Nota'].mean()
print(resposta)

#7 Projeção de Colunas
resposta = df_notas[['Nome', 'Nota']]
print(resposta)

#8 Filtragem por Texto
resposta = df_notas.loc[df_notas['Atividade'] == 'Prova Final']
print(resposta)

#9 Filtragem Composta e Projeção
resposta = df_notas.loc[df_notas['Nota'] > 7, ['Nome', 'Atividade']]
print(resposta)

#10 Ordenação
df_ordenado = df_notas.sort_values(by='Nome')
print(df_ordenado)
 
#11 Junção de DataFrames (Merge)
resposta = pd.merge(df_notas, df_atividades, on='Atividade')
print(resposta)

#12  Exportação de Dados
df_ordenado.to_excel("notas_estudantes_ordenado.xlsx", index=False)
print(df_ordenado)