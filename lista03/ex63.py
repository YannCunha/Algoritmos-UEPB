#Escreva um programa que imprima os N termos de uma Progressão Aritmética, conforme fórmula a seguir. O usuário deverá fornecer o valor de: n (número de termos), r (razão) e a1 (primeiro termo da série).

#a1 = a1
#a2 = a1 + r
#a3 = a2 + r
#a4 = a3 + r
#an = a1 + (n-1).r


n = int(input("Digite o número de termos (n): "))
r = float(input("Digite a razão (r): "))
a1 = float(input("Digite o primeiro termo (a1): "))

print("Os termos da Progressão Aritmética são:")

for i in range(n):
    termo = a1 + i * r
    print(termo, end=" ")
