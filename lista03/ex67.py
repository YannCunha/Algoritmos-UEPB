
#A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:
#a) Média do salário da população;
#b) Média do número de filhos;
#c) Maior salário;
#d) Percentual de pessoas com salário até R$250,00.
#Desenvolver um programa para calcular e escrever o que foi pedido nos itens a, b, c e d. O final da leitura de dados se dará com a entrada de um salário negativo.


total_salario = 0
total_filhos = 0
quantidade_pessoas = 0
maior_salario = 0
pessoas_salario_ate_250 = 0

while True:
    salario = float(input("Digite o salário (negativo para encerrar): "))
#condição para encerrar
    if salario < 0:
        break

    filhos = int(input("Digite o número de filhos: "))
#contagem
    total_salario += salario
    total_filhos += filhos
    quantidade_pessoas += 1
#condição para identificar o maior salario
    if salario > maior_salario:
        maior_salario = salario
#condição para percentual com pessoas com salario menor que 250
    if salario <= 250:
        pessoas_salario_ate_250 += 1

if quantidade_pessoas > 0:
    media_salario = total_salario / quantidade_pessoas
    media_filhos = total_filhos / quantidade_pessoas
    percentual_salario_ate_250 = (pessoas_salario_ate_250 / quantidade_pessoas) * 100
else:
    media_salario = 0
    media_filhos = 0
    percentual_salario_ate_250 = 0

print(f"Média do salário da população: R$ {media_salario:.2f}")
print(f"Média do número de filhos: {media_filhos:.2f}")
print(f"Maior salário: R$ {maior_salario:.2f}")
print(f"Percentual de pessoas com salário até R$250,00: {percentual_salario_ate_250:.2f}%")