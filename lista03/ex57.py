
#57.	Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião em relação ao filme: ótimo - 3, bom - 2, regular - 1. Faça um programa que receba a idade e a opinião de 15 espectadores, calcule e imprima:
#a)	A média das idades das pessoas que responderam ótimo;
#b)	A quantidade de pessoas que responderam regular;
#c)	A porcentagem de pessoas que responderam bom entre todos os espectadores analisados.

#incialização das variaveis
total_idade_otimo = 0
contagem_otimo = 0
contagem_regular = 0
contagem_bom = 0

# Recebe as informações de 15 espectadores
for i in range(15):
    idade = int(input(f"Digite a idade do espectador {i+1}: "))

    # Recebe e valida a opinião
    opiniao_valida = False
    while not opiniao_valida:
        opiniao = int(input("Digite a opinião (ótimo - 3, bom - 2, regular - 1): "))
        if opiniao in [1, 2, 3]:
            opiniao_valida = True
        else:
            print("Opinião inválida. Por favor, digite 1, 2 ou 3.")

    # Calcula a soma das idades e a contagem das opiniões
    if opiniao == 3:
        total_idade_otimo += idade
        contagem_otimo += 1
    elif opiniao == 1:
        contagem_regular += 1
    elif opiniao == 2:
        contagem_bom += 1

# Calcula a média das idades das pessoas que responderam ótimo
media_idade_otimo = total_idade_otimo / contagem_otimo if contagem_otimo > 0 else 0

# Calcula a porcentagem de pessoas que responderam bom
percentual_bom = (contagem_bom / 15) * 100

print(f"A média das idades das pessoas que responderam ótimo é: {media_idade_otimo:.2f}")
print(f"A quantidade de pessoas que responderam regular é: {contagem_regular}")
print(f"A porcentagem de pessoas que responderam bom é: {percentual_bom:.2f}%")