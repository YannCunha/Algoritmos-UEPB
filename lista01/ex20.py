#Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados.

a = int(input("Insira um numero para A: "))
b = int(input("Insira outro numero para B: "))

auxiliar = a
a = b
b = auxiliar

print("A = ", a, "B =",b)