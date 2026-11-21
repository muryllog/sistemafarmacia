import mysql.connector

import mysql.connector
conexao = mysql.connector.connect(
    host="localhost",
    user="root",  #usuario local
    password="root", #senha local
    database="farmacia"
)
if conexao.is_connected():
    print("Conectado ao MySQL!")

cursor = conexao.cursor()


def cliente():
    nome = (input("insira seu nome: "))
    cpf = int((input("insira seu cpf: ")))
    telefone = int((input("insira seu telefone: ")))
    email = (input("insira seu email: "))
    sql = "INSERT INTO clientes (nome, cpf, telefone, email) VALUES (%s, %s, %s, %s)"
    valores = ( nome, cpf, telefone, email)
    cursor.execute(sql, valores)
    conexao.commit()

cliente()
