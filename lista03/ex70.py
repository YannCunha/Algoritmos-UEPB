#Você foi contratado para escrever um algoritmo que calcule quantos pontos fez um time num campeonato de futebol. Para os que não conhecem futebol uma vitória vale três pontos, um empate vale 1 ponto e a derrota não vale ponto. A entrada será composta por pares de números indicando o resultado de cada jogo. O primeiro número sempre corresponde ao total de gols que o time fez no jogo. A leitura dos dados será finalizada quando for fornecido um número de gols negativo.

total_pontos = 0

while True:
    gols_time = int(input("Digite o número de gols do time (número negativo para encerrar): "))

    if gols_time < 0:
        break

    gols_adversario = int(input("Digite o número de gols do adversário: "))

    if gols_time > gols_adversario:
        total_pontos += 3  # Vitória
    elif gols_time == gols_adversario:
        total_pontos += 1  # Empate

print(f"Total de pontos acumulados pelo time: {total_pontos}")