#Escreva um programa que calcula o fatorial de um dado número N.

n = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

for i in range(1, n + 1):
    fatorial *= i
    #equivale a: fatorial = fatorial * i

print(f"O fatorial de {n} é: {fatorial}")