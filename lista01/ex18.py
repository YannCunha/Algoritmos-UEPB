#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7 * altura) – 58."""

altura = int(input("Qual sua altura em centimetros?"))

alturametros = altura / 100
pesoideal = (72.7 * alturametros) - 58

print("Seu peso ideal é:", pesoideal , "kg")
