#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

sexo = str(input("Digite seu sexo com F ou M: "))

sexo = sexo.upper()
if sexo == "F":
  print("FEMININO")
elif sexo == "M":
  print("MASCULINO")
else:
  print("INVÁLIDO")
