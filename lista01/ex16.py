#Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês."""

nome = str(input("Qual o nome do funcionario?"))
salario = float(input("Qual o valor do salario fixo?"))
vendas = float(input("Qual o valor de vendas efetuadas por esse funcionário?"))

salariomes = salario + (vendas * (15/100))

print (nome, "seu salario fixo é R$", salario, ". O seu salario do mês atual é R$", salariomes)
