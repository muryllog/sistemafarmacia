
import mysql.connector
conexao = mysql.connector.connect(
    host="localhost",
    user="root",  #usuario local
    password="1234", #senha local
    database="farmacia"
)
try:
 if conexao.is_connected():
    print("Conectado ao MySQL!")

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
    def selecionar():
         print()
    def atualizar():
        print()

    def deletar():
        print()
 opcao= input(f"1 para utilizar CRUD na tabela cliente\n2 para utilizar na tabela vendas: ")
 match opcao:
   case 1:
     crud_cliente()
   case 2: 
     crud_vendas()
   case _:
     print("Comando inválido")
   
     
except:
  print("Erro ao conectar ao banco de dados")

