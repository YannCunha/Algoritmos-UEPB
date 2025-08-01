#Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N. Faça um programa para gerar e mostrar o número H. 
#O número N será fornecido como entrada.

N = int(input("Digite o valor de N: "))

H = 0

for i in range(1, N + 1):
    H += 1 / i

print(f"O valor de H para N = {N} é: {H:.2f}")