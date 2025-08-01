#Um posto está vendendo combustíveis com a seguinte tabela de descontos:

#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro

#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro.
#Escreva um programa que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é 2,50 o preço do litro do álcool é  R$ 1,90.

numLitros = float(input("numero de litros: "))
tipoCombustivel = input("tipo combustível - A ou G ")

limiteDescontoLitros = 20
valorLitroAlcool = 1.9
valorLitroGasolina = 2.5
descontoAlcoolInferior = 0.97 # (1 - 0.03)
descontoAlcoolSuperior = 0.95 # (1- 0.05)

if tipoCombustivel == "A" or tipoCombustivel == 'a':
    if numLitros <= limiteDescontoLitros:
        valorPago = (numLitros * valorLitroAlcool) * descontoAlcoolInferior
    else:
        valorPago = (numLitros * valorLitroAlcool) * descontoAlcoolSuperior
else:
    if tipoCombustivel == "G" or tipoCombustivel == 'g':
        if numLitros <= limiteDescontoLitros:
            valorPago = (numLitros * valorLitroGasolina) * 0.96
        else:
            valorPago = (numLitros * valorLitroGasolina) * 0.94
    else:
        print("Informação inválida")
        valorPago = 0

print(valorPago)