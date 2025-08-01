#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

# Recebe dois números inteiros do usuário
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Garante que o número menor vem primeiro
inicio = min(numero1, numero2)
fim = max(numero1, numero2)

# Verifica se há números inteiros entre os dois números fornecidos
if inicio + 1 < fim:
    # Gera e exibe os números no intervalo
    print(f"Números inteiros entre {inicio} e {fim}:")
    for numero in range(inicio + 1, fim):
        print(numero, end=" ")
    print()  # Adiciona uma nova linha após a lista de números
else:
    print(f"Não há números inteiros entre {inicio} e {fim}.")