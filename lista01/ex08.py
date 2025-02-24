#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9)."""

farenheit = float(input("Qual a temperatura em Farenheit? "))

celsius = (5 * (farenheit - 32)) / 9

print (farenheit, "°F equivale a", celsius, "°C")