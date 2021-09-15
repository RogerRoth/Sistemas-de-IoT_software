

def main():
    fileArray = []
    lineAverage = ""
    columnAverage = ""

    try:
        file = open("matriz.txt", "r")
        lines = file.readlines()
        
        for line in lines:
            arrayLine = line.split("\t")
            arrayLine = [float(i) for i in arrayLine]
            fileArray.append(arrayLine)
        file.close()

    except:
        print("Arquivo não encontrado!")

    ## Calcula a media das linhas
    for line in fileArray:
        average = sum(line) / len(line)
        if line != fileArray[-1]:
            lineAverage = lineAverage + str(average) + ","
        else:
            lineAverage = lineAverage + str(average)

    fileWrite("average-line.txt", lineAverage)

    ## Calcula a media das colunas
    columnSize = len(fileArray[0])

    for column in range(columnSize):
        sumCol = 0
        for line in fileArray:
            sumCol = sumCol + line[column]

        average = sumCol/len(fileArray)
        if column != columnSize-1:
            columnAverage = columnAverage + str(average) + ","
        else:
            columnAverage = columnAverage + str(average)
                
    fileWrite("average-col.txt", columnAverage)
    
    
    ## Centrar pela média as linhas
    meanCenterLineData = ''

    lineAverage = lineAverage.split(",")
    lineSize = len(fileArray)
    columnSize = len(fileArray[0])

    for line in range(lineSize):

        for column in range(columnSize):
            meanCenterLine = fileArray[line][column] - float(lineAverage[line])
            
            if column != columnSize-1:
                meanCenterLineData = meanCenterLineData + str(meanCenterLine) + ","
            else:
                meanCenterLineData = meanCenterLineData + str(meanCenterLine)
        
        if line != lineSize-1:
            meanCenterLineData = meanCenterLineData + "\n"

    fileWrite("meancenter-line.txt", meanCenterLineData)
    

    ## Centrar pela média as colunasl
    meanCenterColumnData = ''

    columnAverage = columnAverage.split(",")
    lineSize = len(fileArray)
    columnSize = len(fileArray[0])

    for line in range(lineSize):

        for column in range(columnSize):
            
            meanCenterColumn = fileArray[line][column] - float(columnAverage[column])

            if column != columnSize-1:
                meanCenterColumnData = meanCenterColumnData + str(meanCenterColumn) + ","
            else:
                meanCenterColumnData = meanCenterColumnData + str(meanCenterColumn)

        if line != lineSize-1:
            meanCenterColumnData = meanCenterColumnData + "\n"

    fileWrite("meancenter-column.txt", meanCenterColumnData)



def fileWrite(fileName, data):
    try:
        file = open(fileName, "w")
        file.write(data)
        file.close

    except:
        print("Erro ao salvar arquivo!")

if __name__ == "__main__":
    main()