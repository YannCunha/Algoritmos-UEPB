#Faça um Programa que leia três números e mostre o maior deles

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Digite mais um numero: "))

if num1 > num2 and num1 > num3:
  print("O numero maior é:", num1)
elif num2 > num1 and num2 > num3:
  print("O numero maior é:", num2)
elif num3 > num1 and num3 > num2:
  print("O numero maior é:", num3)
else:
  print("Os numeros são iguais")