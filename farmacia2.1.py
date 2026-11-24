import mysql.connector
from datetime import datetime, date
import re
try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        password="root",
        database="farmacia"
    )

    @@ -13,116 +15,173 @@

    cursor = conexao.cursor()

    # função para deixar cpf bunitinhu
    def formatar_cpf(cpf):
        cpf = cpf.replace(".", "").replace("-", "").strip()

        if not cpf.isdigit() or len(cpf) != 11:
            return None

        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    
      # função para validar email
    def validar_email(email):
     formato = r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$"

     if re.fullmatch(formato, email):
        return True
     else:
        return False

      # função para validar a validade do medicamento
    def validar_validade(validade):
        try:
            data_validade = datetime.strptime(validade, "%d/%m/%Y").date()

            if data_validade < date.today():
                return None

            return data_validade.strftime("%Y-%m-%d")

        except ValueError:
            return None

    def inicio():
        opcao = input("1 para utilizar CRUD na tabela cliente\n2 para utilizar na tabela vendas: ")
        print("Digite:")
        opcao = input("1 para utilizar CRUD na tabela cliente.\n2 para utilizar na tabela vendas.\n\n")

        match opcao:
            case "1":
                print("")
                crud_cliente()
            case "2":
                print("")
                crud_vendas()
            case _:
                print("Comando inválido")

    def crud_vendas():

     def cadastrar_med():
        nome = input("Insira o nome do medicamento: ")
        fabricante = input("Insira o fabricante: ")
        preco = float(input("Insira o preço: "))
        while preco <= 0:
          print("Preço inválido! O valor deve ser maior que zero.")
          preco = float(input("Digite o preço: R$ "))
        validade = input("Insira a validade (AAAA-MM-DD): ")
        cpf_cliente = input("Insira o CPF do cliente: ")
        while not cpf_cliente.replace(".", "").replace("-", "").isdigit()or len(cpf_cliente) != 14:
         print("CPF inválido! Digite apenas números, pontos e hífen.")
         cpf_cliente = input("Insira o CPF do cliente: ")
         

        sql = "INSERT INTO medicamentos (nome, fabricante, preco, validade, cpf_cliente) VALUES (%s, %s, %s, %s, %s)"
        valores = (nome, fabricante, preco, validade, cpf_cliente)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Medicamento cadastrado!")

     def selecionar_med():
        sql = "SELECT * FROM medicamentos"
        cursor.execute(sql)

        resultado = cursor.fetchall()

        for medicamento in resultado:
            print("ID:", medicamento[0])
            print("Nome:", medicamento[1])
            print("Fabricante:", medicamento[2])
            print("Preço:", medicamento[3])
            print("Validade:", medicamento[4])
            print("CPF do cliente:", medicamento[5])
        def cadastrar_med():
            nome = input("Insira o nome do medicamento: ")
            fabricante = input("Insira o fabricante: ")
            preco = float(input("Insira o preço: "))

            while preco <= 0:
                print("Preço inválido! O valor deve ser maior que zero.")
                preco = float(input("Digite o preço: R$ "))

            validade = input("Insira a validade (DD/MM/AAAA): ")

            while validar_validade(validade) is None:
                print("Data inválida ou medicamento vencido!")
                validade = input("Insira novamente a validade (DD/MM/AAAA): ")

            validade = validar_validade(validade)

            cpf_cliente = input("Insira o CPF do cliente: ")

            while formatar_cpf(cpf_cliente) is None:
                print("CPF inválido! Digite os 11 números.")
                cpf_cliente = input("Insira o CPF do cliente: ")

            cpf_cliente = formatar_cpf(cpf_cliente)

            sql = "INSERT INTO medicamentos (nome, fabricante, preco, validade, cpf_cliente) VALUES (%s, %s, %s, %s, %s)"
            valores = (nome, fabricante, preco, validade, cpf_cliente)

            cursor.execute(sql, valores)
            conexao.commit()

            print("Medicamento cadastrado!")

        def selecionar_med():
            sql = "SELECT * FROM medicamentos"
            cursor.execute(sql)

            resultado = cursor.fetchall()

            for medicamento in resultado:
                print("----------------------")
                print("ID:", medicamento[0])
                print("Nome:", medicamento[1])
                print("Fabricante:", medicamento[2])
                print("Preço:", medicamento[3])
                print("Validade:", medicamento[4])
                print("CPF do cliente:", medicamento[5])
            print("----------------------")

     def atualizar_med():
        id_med = int(input("Digite o ID do medicamento: "))
        nome = input("Digite o novo nome: ")
        fabricante = input("Digite o novo fabricante: ")
        preco = float(input("Digite o novo preço: "))
        while preco<=0:
          print("Preço inválido! O valor deve ser maior que zero.")
          preco = float(input("Digite o preço: R$ "))
        validade = input("Digite a nova validade (AAAA-MM-DD): ")
        cpf_cliente = input("Digite o novo CPF do cliente: ")
        while not cpf_cliente.replace(".", "").replace("-", "").isdigit()or len(cpf_cliente) != 14:
                 print("CPF inválido! Digite apenas números, pontos e hífen.")
                 cpf_cliente = input("Insira o CPF do cliente: ")
        def atualizar_med():
            id_med = int(input("Digite o ID do medicamento: "))
            nome = input("Digite o novo nome: ")
            fabricante = input("Digite o novo fabricante: ")
            preco = float(input("Digite o novo preço: "))

        sql = "UPDATE medicamentos SET nome=%s, fabricante=%s, preco=%s, validade=%s, cpf_cliente=%s WHERE id_med=%s"
        valores = (nome, fabricante, preco, validade, cpf_cliente, id_med)
            while preco <= 0:
                print("Preço inválido! O valor deve ser maior que zero.")
                preco = float(input("Digite o preço: R$ "))

        cursor.execute(sql, valores)
        conexao.commit()
            validade = input("Insira a validade (DD/MM/AAAA): ")

        print("Medicamento atualizado!")
            while validar_validade(validade) is None:
                print("Data inválida ou medicamento vencido!")
                validade = input("Insira novamente a validade (DD/MM/AAAA): ")

     def deletar_med():
        id_med = int(input("Digite o ID do medicamento: "))
            validade = validar_validade(validade)

        sql = "DELETE FROM medicamentos WHERE id_med=%s"
            cpf_cliente = input("Digite o novo CPF do cliente: ")

        cursor.execute(sql, (id_med,))
        conexao.commit()
            while formatar_cpf(cpf_cliente) is None:
                print("CPF inválido! Digite os 11 números.")
                cpf_cliente = input("Insira o CPF do cliente: ")

        print("Medicamento deletado!")
            cpf_cliente = formatar_cpf(cpf_cliente)

     escolha = input(
        "Digite 1 para cadastrar\n"
        "2 para selecionar\n"
        "3 para atualizar\n"
        "4 para deletar\n"
        "0 para voltar ao menu inicial: "
    )
     sql = "UPDATE medicamentos SET nome=%s, fabricante=%s, preco=%s, validade=%s, cpf_cliente=%s WHERE id_med=%s"
    valores = (nome, fabricante, preco, validade, cpf_cliente, id_med)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Medicamento atualizado!")

    def deletar_med():
            id_med = int(input("Digite o ID do medicamento: "))

            sql = "DELETE FROM medicamentos WHERE id_med=%s"

            cursor.execute(sql, (id_med,))
            conexao.commit()

            print("Medicamento deletado!")

    escolha = input(
            "Digite:\n"
            "1 para cadastrar\n"
            "2 para selecionar\n"
            "3 para atualizar\n"
            "4 para deletar\n"
            "0 para voltar ao menu inicial:\n\n"
        )

    match escolha:
            case "1":
                cadastrar_med()
            case "2":
                selecionar_med()
            case "3":
                atualizar_med()
            case "4":
                deletar_med()
            case "0":
                inicio()
            case _:
                print("Opção inválida")

    match escolha:
        case "1":
            cadastrar_med()
        case "2":
            selecionar_med()
        case "3":
            atualizar_med()
        case "4":
            deletar_med()
        case "0":
            inicio()
        case _:
            print("Opção inválida")
    def crud_cliente():

        def cadastrar():
            nome = input("Insira seu nome: ")

            cpf = input("Insira seu CPF: ")
            while not cpf.replace(".", "").replace("-", "").isdigit()or len(cpf) != 14:
                     print("CPF inválido! Digite apenas números, pontos e hífen.")
                     cpf = input("Insira o CPF do cliente: ")

            while formatar_cpf(cpf) is None:
                print("CPF inválido! Digite os 11 números.")
                cpf = input("Insira seu CPF: ")

            cpf = formatar_cpf(cpf)

            telefone = input("Insira seu telefone: ")
            email = input("Insira seu email: ")

            while not validar_email(email):
              print("Email inválido! Digite novamente.")
              email = input("Insira seu email: ")

            @@ -141,16 +200,22 @@ def selecionar():
            resultado = cursor.fetchall()

            for cliente in resultado:
                print("----------------------")
                print("Nome:", cliente[0])
                print("CPF:", cliente[1])
                print("Telefone:", cliente[2])
                print("Email:", cliente[3])
            print("----------------------")

        def atualizar():
            cpf = input("Digite o CPF do cliente: ")
            while not cpf_cliente.replace(".", "").replace("-", "").isdigit()or len(cpf_cliente) != 14:
                     print("CPF inválido! Digite apenas números, pontos e hífen.")
                     cpf_cliente = input("Insira o CPF do cliente: ")

            while formatar_cpf(cpf) is None:
                print("CPF inválido! Digite os 11 números.")
                cpf = input("Digite o CPF do cliente: ")

            cpf = formatar_cpf(cpf)

            nome = input("Digite o novo nome: ")
            telefone = input("Digite o novo telefone: ")
            email = input("Digite o novo email: ")

            while not validar_email(email):
              print("Email inválido! Digite novamente.")
              email = input("Digite o novo email: ")

            @@ -159,38 +224,51 @@ def atualizar():
            valores = (nome, telefone, email, cpf)

            cursor.execute(sql, valores)
            conexao.commit()

            print("Cliente atualizado com sucesso!")
            if cursor.rowcount == 0:
                print("CPF não encontrado! Nenhum cliente foi atualizado.")
            else:
                conexao.commit()
                print("Cliente atualizado com sucesso!")

        def deletar():
            cpf = input("Digite o CPF do cliente: ")

            while formatar_cpf(cpf) is None:
                print("CPF inválido! Digite os 11 números.")
                cpf = input("Digite o CPF do cliente: ")

            cpf = formatar_cpf(cpf)

            sql = "DELETE FROM clientes WHERE cpf=%s"

            cursor.execute(sql, (cpf,))
            conexao.commit()

            print("Cliente deletado!")

        escolha = input("Digite 1 para cadastrar\n2 para selecionar\n3 para atualizar\n4 para deletar\n0 para voltar ao menu inicial: ")
        escolha = input("Digite:\n1 para cadastrar\n2 para selecionar\n3 para atualizar\n4 para deletar\n0 para voltar ao menu inicial:\n\n")

        match escolha:
            case "1":
                print("")
                cadastrar()
            case "2":
                print("")
                selecionar()
            case "3":
                print("")
                atualizar()
            case "4":
                print("")
                deletar()
            case "0":
                print("")
                inicio()
            case _:
                print("Opção inválida")


    inicio()

except Exception as erro:
    print("Erro:", erro)
    print("Erro:", erro)