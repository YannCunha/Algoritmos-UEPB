#71. Faça um programa que receba um número e verifique se ele é ou não triangular. OBS: um número é triangular quando é resultado do produto de 3 números consecutivos. Exemplo: o número 24 é triangular, pois, 24 = 2 * 3 * 4.

def verificar_triangular(numero):
    if numero < 6:
        return False

    for i in range(1, int(numero**(1/3)) + 2):
        if i * (i + 1) * (i + 2) == numero:
            return True

    return False

numero = int(input("Digite um número para verificar se é triangular: "))

if verificar_triangular(numero):
    print(f"O número {numero} é triangular.")
else:
    print(f"O número {numero} não é triangular.")
