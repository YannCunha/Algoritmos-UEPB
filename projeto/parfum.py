from pymongo import MongoClient, errors
from bson.objectid import ObjectId
from rich.console import Console
from rich.panel import Panel
from tabulate import tabulate

console = Console()

def conectar_banco():
    try:
        client = MongoClient(
            '(LINK BANCO DE DADOS MONGO)',
            serverSelectionTimeoutMS=5000
        )
        db = client.get_database('perfumaria')
        console.print("[green]✔️  Operação realizada com sucesso![/green]")
        return db
    except errors.ConnectionError as e:
        console.print("[red]❌ Ocorreu um erro durante a operação.[/red]")
        return None

def cadastrar_usuario(db, nome, email, senha, tipo_usuario="cliente"):

    if not nome or len(nome.strip()) == 0:
        console.print("[red]❌ Erro: O nome não pode estar vazio.[/red]")
        return

    if not all(c.isalpha() or c.isspace() for c in nome):
        console.print("[red]❌ Erro: O nome deve conter apenas letras e espaços.[/red]")
        return

    if not validar_email(email):
        console.print(f"[red]❌ Erro: O email {email} não é válido. Por favor, insira um email válido.[/red]")
        return

    if db.usuarios.find_one({"email": email}):
        console.print(f"[red]❌ Erro: o email {email} já está cadastrado.[/red]")
        return

    if not senha or len(senha.strip()) < 6:
        console.print("[red]❌ Erro: A senha deve ter pelo menos 6 caracteres.[/red]")
        return

    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "tipo_usuario": tipo_usuario,
    }

    try:
        result = db.usuarios.insert_one(usuario)
        usuario["_id"] = result.inserted_id
        console.print(f"[green]✔️ Usuário {nome} cadastrado com sucesso como {tipo_usuario}![/green]")
        return usuario
    
    except Exception as e:
        console.print(f"[red]❌ Erro ao cadastrar usuário: {e}[/red]")

def buscar_usuario_por_email(db, email):
    usuario = db.usuarios.find_one({"email": email})
    if usuario:
        return usuario
    else:
        console.print("[dim]❓ Usuário não encontrado.[/dim]")
        return None

def autenticar_usuario(db):
    console.print(
            "[bold magenta]💐 Bem-vindo à Perfumaria Sweetscent 💐[/bold magenta]\n",
            justify="center",)
    console.print("[bold purple]==== Login ====[/bold purple]")
    console.print("[bold blue]E-Mail: [/bold blue]", end="")
    email = input()
    console.print("[bold blue]Senha: [/bold blue]", end="")
    senha = input()
    usuario = db.usuarios.find_one({"email": email})

    if usuario and usuario["senha"] == senha:
        print("")
        console.print(f"[green]👋  Bem-vindo, {usuario['nome']}! [/green]")
        
        if usuario.get("is_admin", False):  
            console.print("[yellow]🔑  Você tem permissões de admin. [/yellow]")
            return usuario  # Retorna o usuário com permissões de admin
        else:
            console.print("[blue]👤  Você é um usuário comum. [/blue]")
            return usuario  # Retorna o usuário comum
    else:
        console.print("[red]❌  Credenciais inválidas. [/red]")
        return None

def listar_produtos(db):
    produtos = list(db.produtos.find())
    
    if not produtos:
        print("Nenhum produto disponível.")
        return

    tabela = [
        [i, produto['nome'], f"R${produto['preco']:.2f}", produto['tamanho']] 
        for i, produto in enumerate(produtos, 1)
    ]
    
    headers = ["#", "Nome", "Preço", "tamanho"]
    print("\nProdutos disponíveis:")
    print(tabulate(tabela, headers=headers, tablefmt="grid"))

def adicionar_ao_carrinho(carrinho, db, usuario):
    while True:
        listar_produtos(db)  # Exibe os produtos numerados
        escolha = console.input("\n[cyan]🛒  Escolha o número do produto que deseja adicionar ao carrinho (ou 0 para sair): [/cyan]")
        
        if escolha == "0":
            break

        try:
            escolha = int(escolha) - 1  # Ajuste para o índice correto
            produtos = list(db.produtos.find())
            
            if 0 <= escolha < len(produtos):
                produto = produtos[escolha]
                produto_id = produto["_id"]
                
                # Busca a quantidade do produto no estoque
                estoque = db.estoque.find_one({"produto_id": ObjectId(produto_id)})
                if estoque:
                    quantidade_estoque = estoque["quantidade"]  # Quantidade disponível no estoque
                else:
                    quantidade_estoque = 0  # Caso não haja estoque registrado, assume 0
                
                console.print(f"[green]📦  Estoque disponível para {produto['nome']}: {quantidade_estoque} unidades [/green]")
                quantidade = int(console.input(f"[cyan]➕  Quantas unidades de {produto['nome']} você deseja adicionar? [/cyan]"))

                # Verifica se a quantidade solicitada é maior que a disponível
                if quantidade <= 0:
                    console.print("[red]❌  Quantidade inválida. Não é possível adicionar uma quantidade negativa ou zero. Tente novamente. [/red]")
                elif quantidade > quantidade_estoque:
                    console.print(f"[red]❌  Você não pode adicionar mais do que {quantidade_estoque} unidades. Tente novamente. [/red]")
                else:
                    carrinho.append({"produto": produto, "quantidade": quantidade})
                    console.print(f"[green]✔️  {quantidade} unidades de {produto['nome']} foram adicionadas ao carrinho! [/green]")
            else:
                console.print("[red]❌  Produto não encontrado. [/red]")
        except ValueError:
            console.print("[red]❌  Opção inválida. Tente novamente. [/red]")

def ver_carrinho(carrinho, db, usuario):
    if len(carrinho) == 0:
        console.print("[dim]🛒  Seu carrinho está vazio. [/dim]")
        return

    console.print("\n[bold cyan]🛍️  Carrinho de Compras: [/bold cyan]")
    total = 0
    for item in carrinho:
        produto = item["produto"]
        total += produto["preco"] * item["quantidade"]
        console.print(f"[bold]🛒  {produto['nome']} - Quantidade: {item['quantidade']} - Preço Unitário: R${produto['preco']:.2f}[/bold]")

    print(f"Total: R${total:.2f}")
    finalizar = console.input("\n[bold green]✔️  Deseja finalizar a compra? (s/n): [/bold green]").lower()
    if finalizar == "s":
        finalizar_compra(carrinho, db, usuario, total)

# Função para validar o CEP (8 dígitos numéricos)
def validar_cep(cep):
    # Verifica se o CEP tem exatamente 8 caracteres e se todos são números
    if len(cep) == 8 and cep.isdigit():
        return True
    else:
        return False

def validar_texto_com_espacos(texto):
    if len(texto.strip()) < 3:  # Verifica se o texto tem pelo menos 3 caracteres
        return False

    for char in texto:  # Verifica se todos os caracteres do texto são letras ou espaços
        if not (char.isalpha() or char.isspace()):
            return False

    return True

def validar_numero(numero):  # Função para validar se o número da casa é válido (somente números positivos)
    return numero.isdigit() and int(numero) > 0

def finalizar_compra(carrinho, db, usuario, total):
    # Recolhe os dados do endereço
    while True:
        console.print("\n[bold blue]🏠  Por favor, informe seu endereço de entrega: [/bold blue]")
        cep = console.input("[cyan]📍  CEP (somente números, 8 dígitos): [/cyan]") # Validação do CEP (somente 8 dígitos numéricos)
        if not validar_cep(cep):
            console.print("[red]❌  CEP inválido. O CEP deve conter 8 dígitos numéricos. Tente novamente. [/red]")
            continue

        bairro = console.input("[cyan]🏙️ Bairro: [/cyan]") # Validação do Bairro (texto, pelo menos 3 caracteres)
        if not validar_texto_com_espacos(bairro):
            console.print("[red]❌  Bairro inválido. O nome do bairro deve ter pelo menos 3 caracteres e conter apenas letras. Tente novamente. [/red]")
            continue

        # Validação da Cidade (texto, pelo menos 3 caracteres, aceitando espaços)
        cidade = console.input("[cyan]🏙️  Cidade: [/cyan]")
        if not validar_texto_com_espacos(cidade):
            console.print("[red]❌  Cidade inválida. O nome da cidade deve ter pelo menos 3 caracteres e conter apenas letras. Tente novamente. [/red]")
            continue

        # Validação do Estado (texto, pelo menos 3 caracteres)
        estado = console.input("[cyan]🌍  Estado: [/cyan]")
        if not validar_texto_com_espacos(estado):
            console.print("[red]❌  Estado inválido. O nome do estado deve ter pelo menos 3 caracteres e conter apenas letras. Tente novamente. [/red]")
            continue

        # Validação da Rua (texto, pelo menos 3 caracteres)
        rua = console.input("[cyan]🏠  Rua: [/cyan]")
        if not validar_texto_com_espacos(rua):
            console.print("[red]❌  Rua inválida. O nome da rua deve ter pelo menos 3 caracteres e conter apenas letras. Tente novamente. [/red]")
            continue

        # Validação do Número (somente números positivos)
        numero = console.input("[cyan]🏠  Número da casa: [/cyan]")
        if not validar_numero(numero):
            console.print("[red]❌  Número inválido. O número da casa deve ser um número positivo. Tente novamente. [/red]")
            continue
        
        # Se todos os campos foram validados
        break

    # Previsão de entrega
    console.print("\n[bold green]📅  Previsão de entrega: 3-5 dias úteis. [/bold green]")
    
    # Confirmação de finalização
    confirmar = console.input("[bold green]✔️  Deseja finalizar a compra? (s/n): [/bold green]").lower()
    if confirmar == "s":
        # Criando os itens comprados a partir do carrinho
        itens_comprados = []
        for item in carrinho:
            produto = item["produto"]
            itens_comprados.append({
                "produto_id": ObjectId(produto["_id"]),
                "nome": produto["nome"],
                "preco": produto["preco"],
                "quantidade": item["quantidade"],
                "tamanho": produto["tamanho"]
            })

        # Criando o documento da compra
        compra = {
            "usuario_id": ObjectId(usuario["_id"]),
            "total": total,
            "itens_comprados": itens_comprados,
            "endereco": {
                "cep": cep,
                "bairro": bairro,
                "cidade": cidade,
                "estado": estado,
                "rua": rua,
                "numero": numero
            }
        }

        # Inserindo a compra na coleção de compras
        try:
            resultado_compra = db.compras.insert_one(compra)
            console.print(f"[green]✔️  Compra finalizada com sucesso! Total: R${total:.2f}[/green]")
            console.print("[bold green]🎉  Obrigado pela sua compra![/bold green]")

            # Atualizando o estoque
            for item in carrinho:
                produto = item["produto"]
                quantidade_comprada = item["quantidade"]
                # Atualiza o estoque
                db.estoque.update_one(
                    {"produto_id": ObjectId(produto["_id"])},
                    {"$inc": {"quantidade": -quantidade_comprada}}
                )

            # Inserir itens na coleção de itens_comprados
            for item in carrinho:
                produto = item["produto"]
                db.itens_comprados.insert_one({
                    "compra_id": resultado_compra.inserted_id,
                    "produto_id": ObjectId(produto["_id"]),
                    "quantidade": item["quantidade"],
                    "preco_unitario": produto["preco"]
                })

            # Limpar o carrinho após a compra
            carrinho.clear()

        except Exception as e:
            console.print(f"[red]❌ Erro ao processar a compra: {e}[/red]")

    else:
        console.print("[red]❌ Compra não finalizada. [/red]")
        ver_carrinho(carrinho, db, usuario)

def validar_email(email):
    # Verifica se o e-mail contém '@' e pelo menos um ponto após '@'
    if not email or len(email.strip()) == 0:
        console.print("[red]❌ Erro: O email não pode estar vazio.[/red]")
        return False
    
    if "@" not in email:
        console.print("[red]❌ Erro: O email deve conter o caractere '@'.[/red]")
        return False
    
    nome, dominio = email.split('@', 1)
    
    if '.' not in dominio:
        console.print("[red]❌ Erro: O domínio do e-mail deve conter pelo menos um ponto '.'[/red]")
        return False
    
    if len(nome) == 0 or len(dominio) == 0:
        console.print("[red]❌ Erro: O nome e domínio do e-mail não podem ser vazios.[/red]")
        return False
    
    return True

def obter_entrada(mensagem, tipo, validacao=lambda x: True, erro="Entrada inválida."): # Função genérica para validação de entradas
    """
    Solicita uma entrada do usuário e valida o valor.
    
    args:
        mensagem (str): Mensagem a ser exibida para o usuário.
        tipo (type): O tipo de dado esperado (e.g., int, float, str).
        validacao (callable): Função para validar a entrada (retorna True ou False).
        erro (str): Mensagem de erro para entradas inválidas.
    
    Returns:
        tipo: O valor validado convertido para o tipo desejado.
    """
    while True:
        entrada = input(mensagem)
        try:
            valor = tipo(entrada)
            if validacao(valor):
                return valor
            else:
                print(erro)
        except ValueError:
            print(erro)

# Funções específicas usando a genérica
def obter_preco():
    return obter_entrada(
        "Preço: ",
        float,
        validacao=lambda x: x > 0,
        erro="O preço deve ser um número válido maior que zero.")

def obter_quantidade(mensagem):
    return obter_entrada(
        mensagem,
        int,
        validacao=lambda x: x > 0,
        erro="A quantidade deve ser um número inteiro maior que zero.")

def obter_tamanho():
    while True:
        tamanho = console.input("[bold magenta]🧴 Tamanho: [/bold magenta] ")
        try:
            # Converte para inteiro
            tamanho = int(tamanho)
            
            # Verifica se é maior que 0
            if tamanho > 0:
                return tamanho
            else:
                console.print("[red]❌ Erro: O campo 'tamanho' deve ser maior que 0.[/red]")
        except ValueError:
            console.print("[red]❌ Erro: O campo 'tamanho' deve ser um número inteiro válido.[/red]")

def cadastrar_produto(db, nome, descricao, preco, tamanho, marca, quantidade_inicial):
    """
    Realiza o cadastro de um novo produto e inicializa seu estoque.
    """
    # Validação adicional (redundante, caso já tenha sido validado no menu)
    if not nome or len(nome.strip()) == 0:
        console.print("[red]❌ Erro: O nome do produto não pode ser vazio.[/red]")
        return

    if not descricao or len(descricao.strip()) == 0:
        console.print("[red]❌ Erro: A descrição do produto não pode ser vazia.[/red]")
        return

    if preco <= 0:
        console.print("[red]❌ Erro: O preço deve ser maior que zero.[/red]")
        return
    
    if tamanho <= 0:
        console.print("[red]❌ Erro: A quantidade inicial deve ser maior que zero.[/red]")
        return

    if not marca or len(marca.strip()) == 0:
        console.print("[red]❌ Erro: A marca do produto não pode ser vazia.[/red]")
        return

    if quantidade_inicial <= 0:
        console.print("[red]❌ Erro: A quantidade inicial deve ser maior que zero.[/red]")
        return

    produto = {  # Monta o objeto do produto
        "nome": nome,
        "descricao": descricao,
        "preco": preco,
        "tamanho": tamanho,
        "marca": marca
    }

    try:
        # Insere o produto no banco
        result = db.produtos.insert_one(produto)
        produto_id = result.inserted_id

        # Insere o estoque inicial do produto
        db.estoque.insert_one({
            "produto_id": ObjectId(produto_id),
            "quantidade": quantidade_inicial
        })

        console.print(f"[green]✔️ Produto '{nome}' cadastrado com sucesso com {quantidade_inicial} unidades no estoque![/green]")

    except Exception as e:
        console.print(f"[red]❌ Erro ao cadastrar o produto: {e}[/red]")

# Função para cadastrar produto
def cadastrar_produto_menu(db):
    nome = console.input("[bold blue]📝 Nome: [/bold blue] ")
    descricao = console.input("[bold green]✏️ Descrição: [/bold green] ")
    preco = obter_preco()
    tamanho = obter_tamanho()
    marca = console.input("[bold cyan]🏷️ Marca: [/bold cyan] ")
    quantidade_inicial = obter_quantidade("Quantas unidades deseja adicionar ao estoque? ")
    cadastrar_produto(db, nome, descricao, preco, tamanho, marca, quantidade_inicial)


def atualizar_estoque_menu(db):
    console.print("[bold green]📦 Escolha um produto para atualizar o estoque:[/bold green]")
    produtos = list(db.produtos.find())
    for i, produto in enumerate(produtos, 1):
        print(f"{i}. {produto['nome']}")

    while True:
        try:
            escolha_produto = console.input("[bold blue]🔢 Escolha o número do produto que deseja atualizar o estoque: [/bold blue] ")
            escolha_produto = int(escolha_produto) - 1  # Converte para índice correto

            if 0 <= escolha_produto < len(produtos):
                produto_selecionado = produtos[escolha_produto]
                produto_id = produto_selecionado["_id"]

                # Verifica o estoque atual do produto
                estoque = db.estoque.find_one({"produto_id": ObjectId(produto_id)})
                estoque_atual = estoque["quantidade"] if estoque else 0
                console.print(f"[bold yellow]📊 Estoque atual de {produto_selecionado['nome']}: {estoque_atual} unidades[/bold yellow]")

                # Escolher se quer adicionar ou retirar
                opcao = console.input("[bold magenta]➕ Você deseja adicionar ou retirar unidades? (adicionar/retirar): [/bold magenta]").lower()
                
                if opcao == "adicionar":
                    quantidade_adicionar = int(console.input("[bold green]➕ Quantas unidades deseja adicionar? [/bold green] ").strip())
                    if quantidade_adicionar <= 0:
                        console.print("[bold red]⚠️ A quantidade deve ser maior que zero.[/bold red]")
                        continue
                    novo_estoque = estoque_atual + quantidade_adicionar

                    # Se o estoque não existir, cria o documento de estoque
                    if estoque is None:
                        db.estoque.insert_one({"produto_id": ObjectId(produto_id), "quantidade": novo_estoque})
                        console.print(f"[bold blue]📦 Estoque de {produto_selecionado['nome']} criado com {novo_estoque} unidades.[/bold blue]")
                    else:
                        db.estoque.update_one(
                            {"produto_id": ObjectId(produto_id)},
                            {"$set": {"quantidade": novo_estoque}}
                        )
                        console.print(f"[bold cyan]🔄 Estoque atualizado! Novo estoque de {produto_selecionado['nome']}: {novo_estoque} unidades[/bold cyan]")

                elif opcao == "retirar":
                    quantidade_retirar = int(console.input("[bold red]➖ Quantas unidades deseja retirar? [/bold red] ").strip())

                    if quantidade_retirar <= 0:
                        console.print("[bold red]⚠️ A quantidade deve ser maior que zero.[/bold red]")
                        continue
                    if quantidade_retirar > estoque_atual:
                        console.print(f"[bold red]❌ Erro: Não há estoque suficiente. Estoque atual é de {estoque_atual} unidades.[/bold red]")
                    else:
                        novo_estoque = estoque_atual - quantidade_retirar
                        db.estoque.update_one(
                            {"produto_id": ObjectId(produto_id)},
                            {"$set": {"quantidade": novo_estoque}}
                        )
                        console.print(f"[bold cyan]🔄 Estoque atualizado! Novo estoque de {produto_selecionado['nome']}: {novo_estoque} unidades[/bold cyan]")
                else:
                    console.print("[bold red]❌ Opção inválida. Por favor, digite 'adicionar' ou 'retirar'.[/bold red]")
                break  # Sai do loop após atualizar o estoque
            else:
                console.print("[bold red]❌ Produto não encontrado. Tente novamente.[/bold red]")
        except ValueError:
            console.print("[bold red]❌ Entrada inválida. Por favor, insira um número válido.[/bold red]")

def cadastrar_usuario_admin(db):
    # Função para cadastrar um novo usuário administrador no banco de dados.
    console.print("[bold blue]===== Cadastro de Administrador =====[/bold blue]")
    
    # Validação do nome
    nome = console.input("[bold blue]📝 Nome: [/bold blue] ").strip()
    if not nome or len(nome) == 0 or not all(c.isalpha() or c.isspace() for c in nome):
        console.print("[bold red]❌ Erro: O nome deve conter apenas letras e espaços, e não pode ser vazio.[/bold red]")
        return

    # Validação do email
    email = console.input("[bold cyan]📧 Email: [/bold cyan] ").strip()
    if not email or "@" not in email or len(email) == 0:
        console.print("[bold red]❌ Erro: Insira um email válido.[/bold red]")
        return

    # Validação da senha
    senha = console.input("[bold magenta]🔐 Senha: [/bold magenta] ").strip()
    if not senha or len(senha) < 6:
        console.print("[bold red]❌ Erro: A senha deve ter pelo menos 6 caracteres.[/bold red]")
        return

    # Verificar se o email já está cadastrado
    usuario_existente = db.usuarios.find_one({"email": email})
    if usuario_existente:
        console.print("[bold red]❌ Erro: Já existe um usuário cadastrado com este email.[/bold red]")
        return

    # Criar o usuário admin com o campo `tipo_usuario`
    usuario_admin = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "is_admin": True,  # Indica que o usuário é administrador
        "tipo_usuario": "admin"  # Adicionado para satisfazer o esquema do banco
    }

    try:
        db.usuarios.insert_one(usuario_admin)
        console.print(f"[bold green]✔️ Administrador '{nome}' cadastrado com sucesso![/bold green]")
    except Exception as e:
        console.print(f"[bold red]❌ Erro ao cadastrar administrador: {e}[/bold red]")

def deletar_produto_menu(db):
    console.print("[bold yellow]🗑️ Escolha um produto para deletar:[/bold yellow]")
    produtos = list(db.produtos.find())
    for i, produto in enumerate(produtos, 1):
        print(f"{i}. {produto['nome']}")

    while True:
        try:
            escolha_produto = int(console.input("[bold yellow]🔢 Escolha o número do produto que deseja deletar: [/bold yellow] ").strip()) - 1
            if 0 <= escolha_produto < len(produtos):
                produto_selecionado = produtos[escolha_produto]
                produto_id = produto_selecionado["_id"]

                db.estoque.delete_one({"produto_id": ObjectId(produto_id)})
                db.produtos.delete_one({"_id": ObjectId(produto_id)})

                console.print(f"[bold green]✔️ Produto {produto_selecionado['nome']} deletado com sucesso![/bold green]")

                break
            else:
                console.print("[bold red]❌ Produto não encontrado.[/bold red]")
        except ValueError:
            console.print("[bold red]❌ Entrada inválida. Por favor, insira um número válido.[/bold red]")

def deletar_usuario_menu(db):
    #Função para deletar um usuário do banco de dados.
    console.print("[bold blue]=== Deletar Usuário ===[/bold blue]")
    # Buscar usuários no banco
    usuarios = list(db.usuarios.find())
    if not usuarios:
        console.print("[bold red]❌ Nenhum usuário cadastrado.[/bold red]")
        return
    
    # Exibir a lista de usuários
    console.print("[bold yellow]👥 Usuários cadastrados:[/bold yellow]")
    for i, usuario in enumerate(usuarios, 1):
        console.print(f"[bold cyan]{i}. {usuario['nome']} (Email: {usuario['email']}, Tipo: {usuario['tipo_usuario']})[/bold cyan]")
    
    # Solicitar escolha do usuário a ser deletado
    while True:
        try:
            escolha = int(console.input("[bold yellow]🔢 Escolha o número do usuário que deseja deletar (ou 0 para cancelar): [/bold yellow] ").strip())
            if escolha == 0:
                console.print("[bold red]❌ Operação cancelada.[/bold red]")
                return
            
            if 1 <= escolha <= len(usuarios):
                usuario_selecionado = usuarios[escolha - 1]
                usuario_id = usuario_selecionado["_id"]
                
                # Deletar usuário do banco
                db.usuarios.delete_one({"_id": usuario_id})
                console.print(f"[bold green]✔️ Usuário '{usuario_selecionado['nome']}' deletado com sucesso![/bold green]")
                break
            else:
                console.print("[bold red]❌ Escolha inválida. Tente novamente.[/bold red]")
        except ValueError:
            console.print("[bold red]❌ Entrada inválida. Digite um número válido.[/bold red]")

def relatorio_compras_menu(db):
    """
    Exibe um relatório de compras realizadas.
    """
    console.print("[bold blue]==== Relatório de Compras ====[/bold blue]")
    
    # Buscar todas as compras no banco de dados
    compras = list(db.compras.find())
    
    if not compras:
        console.print("[bold red]❌ Nenhuma compra registrada.[/bold red]")
        return

    # Exibir o relatório de compras
    for compra in compras:
        console.print(f"\n[bold cyan]Compra ID: {compra['_id']}[/bold cyan]")
        console.print(f"[bold green]Total: R${compra.get('total', 0):.2f}[/bold green]")

# Menu admin com dicionário de opções
def menu_admin(db, usuario):
    if not usuario.get('is_admin', False):
        console.print("[bold red]❌ Você não tem permissão para acessar o menu de admin.[/bold red]")
        return

    opcoes = {
    "1": ("Cadastrar Produto", lambda: cadastrar_produto_menu(db)),
    "2": ("Atualizar Estoque", lambda: atualizar_estoque_menu(db)),
    "3": ("Relatório de Compras", lambda: relatorio_compras_menu(db)),
    "4": ("Deletar Produto", lambda: deletar_produto_menu(db)),
    "5": ("Deletar Usuário", lambda: deletar_usuario_menu(db)),
    "6": ("Cadastrar Usuário Admin", lambda: cadastrar_usuario_admin(db)),
    "7": ("Sair", lambda: False)
}

    while True:
        console.print("\n[bold blue]===== Menu Admin =====[/bold blue]")
        for chave, (descricao, _) in opcoes.items():
            console.print(f"[bold cyan]{chave}. {descricao}[/bold cyan]")    
        escolha = console.input("[bold yellow]🔢 Escolha uma opção: [/bold yellow] ")


        if escolha in opcoes:
            _, funcao = opcoes[escolha]
            if escolha == "7":  # Sair
                funcao()
                break
            funcao()
        else:
            console.print("[bold red]❌ Opção inválida. Por favor, escolha novamente.[/bold red]")

# Menu Cliente
def exibir_menu_cliente():
    """Exibe o menu de opções para o cliente."""
    console.print("\n[bold blue]===== Menu Cliente =====[/bold blue]")

    opcoes = {
        "1": "Ver Produtos",
        "2": "Ver Carrinho",
        "3": "Quem Somos?",
        "4": "Ajuda",
        "5": "Sair"
    }
    for chave, descricao in opcoes.items():
        console.print(f"[bold cyan]{chave}. {descricao}[/bold cyan]")

    return opcoes

def menu_cliente(db, usuario):
    carrinho = []

    while True:
        opcoes = exibir_menu_cliente()  # Exibe o menu
        escolha = console.input("[bold yellow]🔢 Escolha uma opção: [/bold yellow] ").strip()


        if escolha == "5":
            console.print("[bold magenta]⏳ Saindo...[/bold magenta]")

            return  # Retorna ao menu de login quando escolher a opção "Sair"
        
        # Dicionário de ações a serem executadas
        acoes = {
            "1": lambda: adicionar_ao_carrinho(carrinho, db, usuario),
            "2": lambda: ver_carrinho(carrinho, db, usuario),
            "3": lambda: console.print("[bold green]🌸 Somos uma perfumaria online com os melhores produtos do mercado.[/bold green]"),
            "4": lambda: console.print("[bold cyan]📧 Contato: Email: perfumaria@exemplo.com, Telefone: (11) 1234-5678.[/bold cyan]"),
        }

        if escolha in opcoes and escolha != "5":
            acoes[escolha]()  # Executa a ação correspondente
        else:
            console.print("[bold red]❌ Opção inválida. Tente novamente.[/bold red]")

# Fluxo Principal
def executar():

    db = conectar_banco()
    console.print("[bold yellow]👋 Bem-vindo ao sistema de gerenciamento de perfumaria![/bold yellow]")

    while True:

        console.print(
            "[bold magenta]💐 Bem-vindo à Perfumaria Sweetscent 💐[/bold magenta]\n",
            justify="center",)

        painel_bemvindo = Panel("[bold white]Escolha uma ação no menu abaixo:[/bold white]",
        border_style="bright_magenta",
        style="bold magenta",
        )
        console.print(painel_bemvindo)

        data = [
            ["1.", "Cadastrar Usuário"],
            ["2.", "Login"],
            ["3.", "Sair"],
        ]

        table = tabulate(data, headers=["Opção, Descrição"], tablefmt="fancy_grid")
        console.print(f"[cyan]{table}[/cyan]")

        console.print("[bold black]🌀 Escolha uma opção: [/bold black]", end="")
        escolha = input()

        if escolha == "1":

            console.print("[bold blue]Nome: [/bold blue]", end="")
            nome = input()
            console.print("[bold blue]E-Mail: [/bold blue]", end="")
            email = input()
            console.print("[bold blue]Senha: [/bold blue]", end="")
            senha = input()

            cadastrar_usuario(db, nome, email, senha)

        elif escolha == "2":
            usuario = autenticar_usuario(db)
            if usuario:
                if usuario.get("is_admin", False):
                    menu_admin(db, usuario)
                else:
                    menu_cliente(db, usuario)

        elif escolha == "3":
            console.print("[bold red]🚪 Saindo do sistema...[/bold red]")
            print("")
            break
        else:
            console.print("[bold black on white]❌ Opção Inválida! Tente novamente. [/bold black on white]")
            print("") 

if __name__ == "__main__":
    executar()
