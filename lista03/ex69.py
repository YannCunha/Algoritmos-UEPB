#O cardápio de uma lanchonete é o seguinte:
#Especificação Código Preço
#Cachorro Quente 100 R$ 1,20
#Bauru Simples 101 R$ 1,30
#Bauru com ovo 102 R$ 1,50
#Hambúrguer 103 R$ 1,20
#Cheeseburguer 104 R$ 1,30
#Refrigerante 105 R$ 1,00

#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

cardapio = {
    100: 1.20,  # Cachorro Quente
    101: 1.30,  # Bauru Simples
    102: 1.50,  # Bauru com ovo
    103: 1.20,  # Hambúrguer
    104: 1.30,  # Cheeseburguer
    105: 1.00   # Refrigerante
}
print ("Cachorro Quente = 100")
print ("Bauru Simples = 101")
print ("Bauru com ovo = 102")
print ("Hambúrguer = 103")
print ("Cheeseburguer = 104")
print ("Refrigerante = 105")
total_geral = 0

#print("Digite 0 para encerrar o pedido.")
while True:
    codigo = int(input("Digite o código do item(Digite 0 para encerrar o pedido): "))

    if codigo == 0:
        break
    elif codigo not in cardapio:
        print("Código inválido! Por favor, digite um código válido ou 0 para encerrar.")
        continue

    quantidade = int(input("Digite a quantidade(Digite 0 para encerrar o pedido): "))

    preco_item = cardapio[codigo]
    valor_pago = preco_item * quantidade

    total_geral += valor_pago

print(f"Total geral do pedido: R$ {total_geral:.2f}")