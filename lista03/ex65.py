
#Faça um programa que receba o valor de uma dívida e mostre uma tabela com
#os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e
#valor da parcela.
#Os juros e a quantidade de parcelas seguem a tabela abaixo:
#Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
#1                                        0
#3                                        10
#6                                        15

#Exemplo de saída do programa:
#Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela
#R$ 1.000,00 0 1 R$ 1.000,00
#R$ 1.100,00 100 3 R$ 366,00
#R$ 1.150,00 150 6 R$ 191,67

divida = float(input("Digite o valor da dívida (R$): "))

#porcntagem dos juros em cada quantidade de parcela
parcelas_juros = {
    1: 0,
    3: 10,
    6: 15
}

#cabeçalho para exibição
print(f"{'Valor da Dívida':<20} {'Valor dos Juros':<15} {'Quantidade de Parcelas':<25} {'Valor da Parcela':<20}")

for parcelas, juros_percentual in parcelas_juros.items():
    valor_juros = (divida * juros_percentual) / 100
    valor_total = divida + valor_juros

    valor_parcela = valor_total / parcelas

    print(f"R$ {valor_total:<18,.2f} R$ {valor_juros:<14,.2f} {parcelas:<24} R$ {valor_parcela:<18,.2f}")