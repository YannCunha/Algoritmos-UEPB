#Faça um programa para somar os números pares positivos < 1000 e ao final escrever o resultado.

soma = 0

#inicializa a partir do 2, ate o 1000, com passo de 2 em 2
for num in range(2, 1000, 2):
    soma += num

print(f"A soma dos números pares positivos menores que 1000 é: {soma}")