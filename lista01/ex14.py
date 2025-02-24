#Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto."""

distancia =  float(input("Qual foi a distancia percorrida? "))
litro = float(input("Qual a quantidade de combustivel utilizada?"))

consumomedio = distancia / litro

print ("O consumo medio do seu carro é", consumomedio , "km/L")