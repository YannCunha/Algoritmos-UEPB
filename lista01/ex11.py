#Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. 
# Considere fixo o juro da poupança em 0,70% a. m."""

valordep = float(input("Qual o valor depositado? "))
rendi = valordep + (valordep * (0.7/100))
print ("Com rendimento, você tem R$", rendi)