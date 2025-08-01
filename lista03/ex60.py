#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero = int(input("Digite um número inteiro: "))

primo = True

#condição para 1,0 e numeros negtivos
if numero <= 1:
    primo = False
else:
    i = 2
    #verificação se é primo
    while i <= int(numero ** 0.5):
        if numero % i == 0:
            primo = False
        i += 1

if primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
