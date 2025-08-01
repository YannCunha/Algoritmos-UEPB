#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperatura informada, bem como a média das temperaturas.

#inicialização das variaveis
menor_temperatura = None
maior_temperatura = None
soma_temperaturas = 0
quantidade_temperaturas = 0

while True:
    entrada = input("Digite a temperatura (ou 'fim' para encerrar): ")
#condição para finalizar com FIM ou fim
    if entrada.lower() == 'fim':
        break
#converter a entrada em float e quando não for possivel exibe "entrada invalida"
#devido o ValueError e "continue" para que peça uma entrada valida
    try:
        temperatura = float(entrada)
    except ValueError:
        print("Entrada inválida! Por favor, digite um número ou 'fim' para encerrar.")
        continue

    if menor_temperatura is None or temperatura < menor_temperatura:
        menor_temperatura = temperatura
    if maior_temperatura is None or temperatura > maior_temperatura:
        maior_temperatura = temperatura

    soma_temperaturas += temperatura
    #soma total das temperaturas
    quantidade_temperaturas += 1
    #contador de temperaturas

if quantidade_temperaturas > 0:
    media_temperaturas = soma_temperaturas / quantidade_temperaturas
    print(f"A menor temperatura informada foi: {menor_temperatura:.2f}")
    print(f"A maior temperatura informada foi: {maior_temperatura:.2f}")
    print(f"A média das temperaturas é: {media_temperaturas:.2f}")
else:
    print("Nenhuma temperatura foi informada.")
