#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#a)salário bruto; b)quanto pagou ao INSS.
#c)quanto pagou ao sindicato. d)o salário líquido.
#e)	calcule os descontos e o salário líquido, conforme a tabela abaixo:

#Salário Bruto : R$
#IR (11%) : R$
#INSS (8%) : R$
#Sindicato ( 5%) : R$
#Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

horastrabalhadas = int(input("Qual o total de horas trabalhadas? "))
valorhora = float(input("Qual o valor da hora trabalhada? "))

salariobruto =  horastrabalhadas * valorhora
IR = salariobruto * (11/100)
INSS = salariobruto * (8/100)
sindicato = salariobruto * (5/100)
salarioliquido = salariobruto - IR - INSS - sindicato

print ("Salario bruto: R$" , salariobruto)
print ("Desconto INSS: R$" , INSS)
print ("Desconto IR: R$", IR)
print ("Desconto sindicato: R$", sindicato)
print ("Sendo assim o salario do mês é: R$", salarioliquido)