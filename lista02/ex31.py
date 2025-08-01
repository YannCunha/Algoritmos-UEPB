#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.  """

diadasemana = int(input("Digite um numero de 1 a 7: "))

if diadasemana == 1:
  print("Domingo")
elif diadasemana == 2:
  print("Segunda-feira")
elif diadasemana == 3:
  print("Terça-feira")
elif diadasemana == 4:
  print("Quarta-feira")
elif diadasemana == 5:
  print("Quinta-feira")
elif diadasemana == 6:
  print("Sexta-feira")
elif diadasemana == 7:
  print("Sábado")
else:
  print("Valor inválido")