

#Uma grande firma deseja saber qual é o empregado mais recente e qual é o mais antigo. Desenvolver um programa para ler um número indeterminado de informações contendo o número do empregado e o número de meses de trabalho deste empregado e imprimir o mais recente e o mais antigo. Obs.: A última informação contém os dois números iguais a zero. Não existem dois empregados admitidos no mesmo mês.

# Inicialização de variáveis
mais_recente_empregado = None
mais_recente_meses = None
mais_antigo_empregado = None
mais_antigo_meses = None

empregados_inseridos = set()  # Conjunto para armazenar números de empregados já inseridos

# Loop para ler os dados dos empregados
while True:
    numero_empregado = int(input("Digite o número do empregado (ou 0 para encerrar): "))

    # Condição de parada: ambos valores iguais a zero
    if numero_empregado == 0:
        break
    # Verifica se o número do empregado já foi inserido
    if numero_empregado in empregados_inseridos:
        print("Número do empregado já inserido. Por favor, insira um número diferente.")
        continue
    #Loop para que não haja inserção de meses negativos
    meses_trabalho = int(input("Digite o número de meses de trabalho: "))
    while meses_trabalho < 0:
        print("Número de meses inválido. Por favor, insira um número positivo.")
        meses_trabalho = int(input("Digite o número de meses de trabalho: "))

    # Adiciona o número do empregado ao conjunto de inseridos
    empregados_inseridos.add(numero_empregado)

    # Verifica se é o empregado mais recente
    if mais_recente_meses is None or meses_trabalho < mais_recente_meses:
        mais_recente_empregado = numero_empregado
        mais_recente_meses = meses_trabalho

    # Verifica se é o empregado mais antigo
    if mais_antigo_meses is None or meses_trabalho > mais_antigo_meses:
        mais_antigo_empregado = numero_empregado
        mais_antigo_meses = meses_trabalho

# Exibe os resultados
if mais_recente_empregado is not None and mais_antigo_empregado is not None:
    print(f"\nEmpregado mais recente: {mais_recente_empregado} (Meses de trabalho: {mais_recente_meses})")
    print(f"Empregado mais antigo: {mais_antigo_empregado} (Meses de trabalho: {mais_antigo_meses})")
else:
    print("Nenhum dado de empregado foi inserido.")
