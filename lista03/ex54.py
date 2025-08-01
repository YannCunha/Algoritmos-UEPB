#Fazer um programa que calcule e escreva a soma dos 50 primeiros termos da seguinte série:

# Inicializa a variável para armazenar a soma
soma = 0

# Calcula a soma dos 50 primeiros termos da série
for i in range(1, 51):
    numerador = 1000 - 3 * (i - 1)
    denominador = i
    soma += numerador / denominador

# Exibe o resultado com apenas 2 casas decimais
print(f"A soma dos 50 primeiros termos da série é: {soma:.2f}")