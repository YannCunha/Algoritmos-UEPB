#Faça um programa que mostre os n termos da Série a seguir:
#S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
#Imprima no final a soma da série.

n = int(input("Digite o número de termos n: "))

soma = 0
denominador = 1

print("Termos da série:")
for i in range(1, n + 1):
    termo = i / denominador
    soma += termo
    print(f"{i}/{denominador}", end=" ")
    #condição para entrada menor que o denominador 1
    if i < n:
        print("+", end=" ")
    # Atualiza o denominador para o próximo termo
    denominador += 2

print("\nA soma da série é:", soma)