#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

n = int(input("Digite o número de pessoas: "))

#inicialização da varivel
soma_idades = 0

#repetição de vezes em relação ao numero de pessoas
for a in range(n):
    idade = int(input("Digite a idade: "))
    soma_idades += idade

media_idades = soma_idades / n

#conidções para verificação da classificação
if media_idades <= 25:
    classificacao = "jovem"
elif 26 <= media_idades <= 60:
    classificacao = "adulta"
else:
    classificacao = "idosa"

print(f"A média de idade da turma é {media_idades:.2f}. A turma é {classificacao}.")
