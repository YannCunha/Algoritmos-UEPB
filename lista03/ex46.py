#Escreva um programa que calcula a média de 30 alunos e informa a situação (reprovado, aprovado ou recuperação).

notas = 0
n = 30

#Recebendo 30 notas
for i in range (30):
  nota = float(input("Digite sua nota: "))
  notas = nota + notas

#Calculo da media
media = notas / n
print("A media da turma é: ", media)

#Verificando a Situação
if media >= 7:
  print("Aprovado")
elif media >= 5:
  print("Recuperação")
else:
  print("Reprovado")
