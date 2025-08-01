#Faça um programa que leia uma quantidade não determinada de números positivos. Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos números lidos. O número que encerrará a leitura será zero."""

soma_pares = 0
soma_total = 0
quantidade_pares = 0
quantidade_impares = 0
quantidade_numeros = 0

while True:
    numero = float(input("Digite um número positivo (0 para encerrar): "))

    if numero == 0:
        break

    if numero < 0:
        print("Número inválido! Por favor, digite um número positivo.")
        continue

    quantidade_numeros += 1
    soma_total += numero

    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1

if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
else:
    media_pares = 0

if quantidade_numeros > 0:
    media_geral = soma_total / quantidade_numeros
else:
    media_geral = 0

print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
print(f"Média dos valores pares: {media_pares:.2f}")
print(f"Média geral dos números lidos: {media_geral:.2f}")