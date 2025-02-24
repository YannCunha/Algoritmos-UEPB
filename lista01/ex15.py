#Escreva um programa que leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão: D = (R + S) / 2, onde, R = (A + B)^2 e S = (B + C)^2

a = float(input("Qual o valor de A? "))
b = float(input("Qual o valor de B? "))
c = float(input("Qual o valor de C? "))

r = (a + b) ** 2
s = (b + c) ** 2

d = (r + s) / 2

print ("O valor final da expressão é ", d)