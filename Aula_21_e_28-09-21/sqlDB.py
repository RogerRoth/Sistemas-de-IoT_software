# arquivo de funções e conexões do banco de dados relacional
'''
Host: sql10.freesqldatabase.com
Database name: sql10440610
Database user: sql10440610
Database password: 9vVIK9d3qA
Port number: 3306

'''
import pyodbc

import mysql.connector

cnx = mysql.connector.connect(
    user='sql10440610', password='9vVIK9d3qA',
    host='sql10.freesqldatabase.com',
    database='sql10440610'
)

cursor = cnx.cursor()

#CREATE TABLE `sql10440610`.`Pessoa` ( `id` INT NOT NULL AUTO_INCREMENT , `nome` VARCHAR NOT NULL , `idade` VARCHAR NOT NULL , `altura` VARCHAR NOT NULL , `pais` VARCHAR NOT NULL , PRIMARY KEY (`id`(8))) ENGINE = InnoDB;
'''
pessoa = [{
    'nome': 'Maria Eduarda',
    'idade': '20',
    'altura': '1.60',
    'pais': 'Brasil'
    },
    {
    'nome': 'Laura Giovanna',
    'idade': '30',
    'altura': '1.80',
    'pais': 'Brasil'
    },
]

cursor.execute("INSERT INTO Pessoa (nome, idade, altura, pais) VALUES (%s, %s, %s, %s)", (pessoa[0]['nome'], pessoa[0]['idade'], pessoa[0]['altura'], pessoa[0]['pais'])) 
cursor.execute("INSERT INTO Pessoa (nome, idade, altura, pais) VALUES (%s, %s, %s, %s)", (pessoa[1]['nome'], pessoa[1]['idade'], pessoa[1]['altura'], pessoa[1]['pais'])) 

cnx.commit()


cursor.close()
cnx.close()
'''


cursor.execute("SELECT * FROM `Pessoa`")

