

import mysql.connector

try:
 conexao = mysql.connector.connect(
    host="localhost",
    user="root",  #usuario local
    password="root", #senha local
    password="1234", #senha local
    database="farmacia"
 )
 if conexao.is_connected():  
   
 
    if conexao.is_connected():
     print("Conectado ao MySQL!")

 cursor = conexao.cursor()
 cursor = conexao.cursor()

 def crud_cliente():
    

  def cadastrar(): 
     nome = (input("insira seu nome: "))
     cpf = int((input("insira seu cpf: ")))
     telefone = int((input("insira seu telefone: ")))
     email = (input("insira seu email: "))
     sql = "INSERT INTO clientes (nome, cpf, telefone, email) VALUES (%s, %s, %s, %s)"
     valores = ( nome, cpf, telefone, email)
     cursor.execute(sql, valores)
     conexao.commit()
     print("Cliente Cadastrado!")

  def selecionar():
        sql = "SELECT * FROM clientes"
        cursor.execute(sql)

        resultado = cursor.fetchall()

        for cliente in resultado:
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

     print("Cliente atualizado com sucesso!")
   
  def deletar():
   print()
   opcao= input(f"1 para utilizar CRUD na tabela cliente\n2 para utilizar na tabela vendas: ")
 match opcao:
     case "1":
      crud_cliente()
     case "2": 
      crud_vendas()
     case _:
      print("Comando inválido")
   
     
     
except:
 print("Erro ao conectar ao banco de dados")

