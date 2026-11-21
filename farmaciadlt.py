import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root", #seu usuario
        password="root", #sua senha
        database="farmacia"
    )

    if conexao.is_connected():
        print("Conectado ao MySQL!")

    cursor = conexao.cursor()

    def crud_cliente():

        def cadastrar():
            nome = input("Insira seu nome: ")
            cpf = input("Insira seu CPF: ")
            telefone = input("Insira seu telefone: ")
            email = input("Insira seu email: ")
            sql = "INSERT INTO clientes (nome, cpf, telefone, email) VALUES (%s, %s, %s, %s)"
            valores = (nome, cpf, telefone, email)
            cursor.execute(sql, valores)
            conexao.commit()
            print("cliente cadastrado!")

        def selecionar():
            sql = "SELECT * FROM clientes"
            cursor.execute(sql)
            resultado = cursor.fetchall()

            for cliente in resultado:
                print("___________________")
                print("Nome:", cliente[0])
                print("CPF:", cliente[1])
                print("Telefone:", cliente[2])
                print("Email:", cliente[3])
                

        def atualizar():
            cpf = input("Digite o CPF do cliente: ")
            nome = input("Digite o novo nome: ")
            telefone = input("Digite o novo telefone: ")
            email = input("Digite o novo email: ")

            sql = "UPDATE clientes SET nome=%s, telefone=%s, email=%s WHERE cpf=%s"
            valores = (nome, telefone, email, cpf)
            cursor.execute(sql, valores)
            conexao.commit()
            print("cliente atualizado com sucesso!")

        def deletar():
            cpf = input("Digite o CPF do cliente que deseja excluir: ")
            sql = "DELETE FROM clientes WHERE cpf=%s"
            cursor.execute(sql, (cpf,))
            conexao.commit()
            print("Cliente excluído com sucesso!")

        # Menu do CRUD de clientes
        print("\n--- CRUD CLIENTES ---")
        print("1 - Cadastrar")
        print("2 - Selecionar")
        print("3 - Atualizar")
        print("4 - Deletar")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                cadastrar()
            case "2":
                selecionar()
            case "3":
                atualizar()
            case "4":
                deletar()
            case _:
                print("Comando inválido")

    def crud_vendas():
        print("CRUD de vendas ainda não implementado.")

    # Menu principal
    print("\n--- MENU PRINCIPAL ---")
    print("1 - CRUD Cliente")
    print("2 - CRUD Vendas")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            crud_cliente()
        case "2":
            crud_vendas()
        case _:
            print("Comando inválido")

except Exception as e:
    print(f"Erro: {e}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()