#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: para homens: (72.7*h) – 58 e para mulheres: (62.1*h) - 44.7 (h = altura)

sexo = str(input("Digite M para masculino e F para feminino:"))
sexo = sexo.upper()
altura = int(input("Digite sua altura em centimetros:"))

h = altura / 100

if sexo == "M":
  peso = (72.7 * h) - 58
  print ("Seu peso ideal é ", peso)
elif sexo == "F":
  peso = (62.1 * h) - 44.7
  print ("Seu peso ideal é ", peso)
else:
  print("Sexo Invalido")