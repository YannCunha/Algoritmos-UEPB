#Faça um programa que recebe o número real x como entrada e devolva uma aproximação do arco tangente de x (em radianos) através da série:

x = float(input("Digite o valor de x: "))

#iniciação da variavel para receber o numero real
aproximacao = 0

for n in range(50):
    termo = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
    aproximacao += termo

print(f"A aproximação do arco tangente de {x} é: {aproximacao:.2f} radianos")