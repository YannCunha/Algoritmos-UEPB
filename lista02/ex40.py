#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

numero = float(input("Digite um numero: "))
parte_inteira = int(numero)

if parte_inteira % 2 == 0:
  print("Esse numero é par")
else:
  print("Esse numero é impar")

if numero > 0:
  print("Esse numero é positivo")
else:
  print("Esse numero é negativo")

if numero % 1 == 0:
  print("Esse numero é inteiro")
else:
  print("Esse numero é decimal")
