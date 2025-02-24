#Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o usuário."""

cotdolar = float(input("Qual a cotação atual do dolar em real? "))
qtddolar = int(input("Qual a quantidade de dolares para a troca? "))

conversao = cotdolar * qtddolar

print ("O valor final é R$", conversao)