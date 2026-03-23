#Comando continue: Ignora o restante dos comandos
#Dentro do loop e continua do início na próxima interação 

#dic de estudantes
aluno1 = {"nome": "Pablo", "idade": 17, "sexo": "M"}
aluno2 = {"nome": "Samara", "idade": 17, "sexo": "F"}
aluno3 = {"nome": "Carlos", "idade": 18, "sexo": "M"}

#lista de dic
alunos = [aluno1, aluno2, aluno3]

for aluno in alunos:
    if aluno['idade'] >= 18:
        continue
    print("Olá", aluno['nome'], "qual é seu passatempo?")
    aluno['hobbie'] = input('')

print(alunos)