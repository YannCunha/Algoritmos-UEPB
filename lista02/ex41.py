#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#Telefonou para a vítima?"
#Esteve no local do crime?"
#Mora perto da vítima?"
#Devia para a vítima?"
#Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print ("Responda as perguntas com 1 para sim e 0 para não")

telef = int(input("Telefonou para a vítima? "))
local = int(input("Esteve no local do crime? "))
mora = int(input("Mora perto da vítima? "))
devia = int(input("Devia para a vítima? "))
trabalhou = int(input("Já trabalhou com a vítima? "))
if telef > 1 or local > 1 or mora > 1 or devia > 1 or trabalhou > 1:
  print("Resposta Invalida, deve ser respondido apenas com 0 e 1")
elif telef < 0 or local < 0 or mora < 0 or devia < 0 or trabalhou < 0:
  print("Resposta Invalida, deve ser respondido apenas com 0 e 1")
elif telef + local + mora + devia + trabalhou == 5:
  print("Assassino")
elif telef + local + mora + devia + trabalhou == 4 or telef + local + mora + devia + trabalhou == 3:
  print("Cúmplice")
elif telef + local + mora + devia + trabalhou == 2:
  print("Suspeita")
else:
  print("Inocente")