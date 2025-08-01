#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.


media1 = float(input("Digite sua primeira nota: "))
media2 = float(input("Digite sua segunda nota: "))

media = (media1 + media2) / 2

if media == 10:
  print("Aprovado com Distinção")
elif media > 10:
  print("Nota inválida")
elif media >= 7:
  print("Aprovado")
else:
  print("Reprovado")