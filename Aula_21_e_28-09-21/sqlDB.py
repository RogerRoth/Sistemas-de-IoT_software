# arquivo de funções e conexões do banco de dados relacional
'''
Host: sql10.freesqldatabase.com
Database name: sql10440610
Database user: sql10440610
Database password: 9vVIK9d3qA
Port number: 3306

'''
import mysql.connector

cnx = mysql.connector.connect(
    user='sql10440610', password='9vVIK9d3qA',
    host='sql10.freesqldatabase.com',
    database='sql10440610'
)

cursor = cnx.cursor()

def insertRegister(pessoa):
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO Pessoa (nome, idade, altura, pais) VALUES (%s, %s, %s, %s)", (pessoa['nome'], pessoa['idade'], pessoa['altura'], pessoa['pais']))
    cnx.commit()

    cursor.close()
    print('Registro inserido com sucesso!')


def buscaTodosRegistros():
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM Pessoa")
    result = cursor.fetchall()
    aux = []
    for i in result:
        aux.append(i)

    cursor.close()
    return aux
