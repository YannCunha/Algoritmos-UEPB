#Escreva um programa que leia 10 números e informe o maior e o menor número.

#inicializando a variavel sem valor
maior = None
menor = None

#Entrada de 10 numeros
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
#Verificação do maior e do menor
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
