#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
#O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

# Solicita ao usuário o número para gerar a tabuada e garante que esteja no intervalo permitido
while True:
    numero = int(input("Digite um número inteiro entre 1 e 10 para ver a tabuada: "))

    if 1 <= numero <= 10:
        print(f"TABUADA DE {numero}:")

          # Inicializa o contador
        i = 1

          # Gera e exibe a tabuada usando o loop while
        while i <= 10:
            print(f"{numero} X {i} = {numero * i}")
            i += 1
        break
    else:
        print("Número fora do intervalo. Por favor, digite um número entre 1 e 10.")