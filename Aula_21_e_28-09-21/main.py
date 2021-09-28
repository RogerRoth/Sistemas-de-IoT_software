import noSQLDB
import sqlDB


def sincSQLData(noSQLData, sqlDBData):
    for pessoa in noSQLData:
        add = False

        for compare in sqlDBData:
            if(compare[1] == pessoa['nome'] and compare[2] == pessoa['idade'] and compare[3] == pessoa['altura'] and compare[4] == pessoa['pais']):
                add = False
                print(add)
                break
            else:
                add = True
                print(add)

        print('saiu')
        if(add):
            sqlDB.insertRegister(pessoa)

def sincNoSQLDB(noSQLData, sqlDBData):
    for compare in sqlDBData:
        add = False

        for pessoa in noSQLData:
            if(compare[1] == pessoa['nome'] and compare[2] == pessoa['idade'] and compare[3] == pessoa['altura'] and compare[4] == pessoa['pais']):
                add = False
                print(add)
                break
            else:
                add = True
                print(add)

        print('saiu')
        if(add):
            print({
            'nome': 'Laura Giovanna',
            'idade': '30',
            'altura': '1.80',
            'pais': 'Brasil'
            })
            #noSQLDB.insertRegister(pessoa)


def main ():
    noSQLData = noSQLDB.buscaTodosRegistros()
    sqlDBData = sqlDB.buscaTodosRegistros()

    #sincSQLData(noSQLData, sqlDBData)

    sincNoSQLDB(noSQLData, sqlDBData)

main()