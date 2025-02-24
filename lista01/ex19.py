#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em MBps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

arquivo = float(input("Qual o tamanho do arquivo em MB? "))
internet = float(input("Qual a velocidade da sua internet em MBps? "))

temposegundo = arquivo / (internet / 8) #calcula o tempo em segundos
tempominuto =  temposegundo / 60 #conversão de segundos para minutos

print ("O arquivo será baixado em", tempominuto, "minutos")