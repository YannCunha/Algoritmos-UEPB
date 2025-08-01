
#Faça um programa para validar o login e a senha de um usuário. Caso o usuário informe algum valor inválido informar o erro e pedir novamente os dados. A leitura dos dados deve ser encerrada quando digitar 3 vezes um valor inválido (login ou senha). Considere o login válido como "kezia" e a senha como "123"."""

login_valido = "kezia"
senha_valida = "123"

tentativas_invalidas = 0
max_tentativas_invalidas = 3

while tentativas_invalidas < max_tentativas_invalidas:
    login = input("Digite o login: ")
    login1 = login.lower()
    senha = input("Digite a senha: ")

    if login1 == login_valido and senha == senha_valida:
        print("Login e senha válidos!")
        break
    else:
        print("Login ou senha inválidos.")
        tentativas_invalidas += 1

if tentativas_invalidas == max_tentativas_invalidas:
    print("Número máximo de tentativas inválidas alcançado. Encerrando o programa.")