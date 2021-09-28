import noSQLDB
import sqlDB


def sincSQLData(noSQLData, sqlDBData):
    for pessoa in noSQLData:
        add = False

        for compare in sqlDBData:
            if(compare[1] == pessoa['nome'] and compare[2] == pessoa['idade'] and compare[3] == pessoa['altura'] and compare[4] == pessoa['pais']):
                add = False
                break
            else:
                add = True

        if(add):
            sqlDB.insertRegister(pessoa)

def sincNoSQLDB(noSQLData, sqlDBData):
    for compare in sqlDBData:
        add = False

        for pessoa in noSQLData:
            if(compare[1] == pessoa['nome'] and compare[2] == pessoa['idade'] and compare[3] == pessoa['altura'] and compare[4] == pessoa['pais']):
                add = False
                break
            else:
                add = True

        if(add):
            noSQLDB.insertRegister(compare)


def main ():
    noSQLData = noSQLDB.buscaTodosRegistros()
    sqlDBData = sqlDB.buscaTodosRegistros()

    sincSQLData(noSQLData, sqlDBData)

    sincNoSQLDB(noSQLData, sqlDBData)

main()