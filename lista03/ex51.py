#Faça um programa para calcular um valor A elevado a um expoente B. Os valores A e B deverão ser lidos. Não usar A** B e sim uma estrutura de repetição.

A = float(input("Digite o valor de A: "))
B = int(input("Digite o valor de B (deve ser um número inteiro): "))

resultado = 1

for e in range(abs(B)):
    resultado *= A
    #equivale a: resultado = resultado * a
if B < 0:
    resultado = 1 / resultado

print(f"O valor de {A} elevado a {B} é: {resultado}")