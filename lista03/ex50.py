#Faça um programa para calcular a área de N quadriláteros. Fórmula: Área = Lado * Lado.

N = int(input("Digite o número de quadriláteros: "))
#precauções para entradas "indevidas"
if N <= 0:
    print("O número de quadriláteros deve ser maior que zero.")
elif N < 0:
    print("O número de quadriláteros não pode ser negativo.")
else:
#repetição para o numero de vezes solicitados pela entrada
    for i in range(N):
        lado = float(input(f"Digite o comprimento do lado do quadrilátero {i+1}: "))
        #calculo da area
        area = lado * lado
        print(f"A área do quadrilátero {i+1} é: {area}")