#Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário."""

custo = float(input("Qual o valor de custo do produto? "))
lucro = int(input("Qual o percentual de acrescimo para o valor de venda?"))

valorvenda = custo + (custo * (lucro/100))

print("O valor de venda do produto é R$" ,  valorvenda)
