#Pandas: biblioteca em Python que permite a manipulação de arquivos em formato tabular. Ex: planilhas e tabelas.
#edição de dados (inserir, atualizar e excluir)

#importar a biblioteca ('as' renomeia o pacote)
import pandas as pd

#ler uma planilha do Excel
#cria a variável planilha que irá guardar a planilha do Excel
#em pandas chamamos a planilha de DataFrame
planilha = pd.read_excel("aula9\\Dados_3INFOB.xlsx")

#mostra todos os dados da planilha
print(planilha)

#imprime a cabeça da planilha: quantas linhas da parte de cima eu quero imprimir
#print(planilha.head(4))

#imprimir as últimas 3 linhas
#print(planilha.tail(5))

#cria uma nova planilha com os dados da cabeça da 1º planilha
nova = (planilha.head(4))
print(nova.tail(2))

#inserir um novo registro
planilha.loc[len(planilha)] = ['Pablo', 52, 1.8, 'M']
print(planilha)

#atualizar um registro
planilha.loc[16] = ['Pablo', 52, 1.8, 'Masculino']
print(planilha)

#atualizar um registro em apenas uma coluna
planilha.loc[16, 'Nome'] = 'Pablo Sandi'
print(planilha)

#atualizar um registro em duas ou mais colunas
planilha.loc[16, ['Peso', 'Altura']] = [53, 1.81]
print(planilha)

#remover um dado da planilha
planilha.drop(13, inplace=True)
print(planilha)
