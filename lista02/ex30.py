#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20%
#Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#i.	Salário Bruto: (5 * 220)        : R$ 1100,00
#ii.	(-) IR (5%)                     : R$   55,00  
#iii.	(-) INSS ( 10%)                 : R$  110,00
#iv.	FGTS (11%)                      : R$  121,00
#v.	Total de descontos              : R$  165,00
#vi.	Salário Liquido                 : R$  935,00


horastrabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valorhora = float(input("Digite o valor da hora trabalhada: "))

salariobruto = horastrabalhadas * valorhora
print("Salário Bruto: R$", salariobruto)
if salariobruto <= 900:
  IR = 0
  print("(-) IR (isento)")
elif salariobruto > 900 and salariobruto <= 1500:
  IR = salariobruto * 0.05
  print("(-) IR (5%): R$", IR)
elif salariobruto > 1500 and salariobruto <= 2500:
  IR = salariobruto * 0.1
  print("(-) IR (10%): R$", IR)
else:
  IR = salariobruto * 0.2
  print("(-) IR (20%): R$", IR)

INSS = salariobruto * 0.1
FGTS = salariobruto * 0.11
sindicato = salariobruto * 0.03
descontos = IR + INSS + sindicato
salarioliquido = salariobruto - descontos

print("(-) INSS (10%): R$", INSS)
print("(-) Sindicato (3%): R$", sindicato)
print("FGTS (11%): R$", FGTS)
print("Total de descontos: R$", descontos)
print("Salário Liquido: R$", salarioliquido)