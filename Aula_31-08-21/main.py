'''
Aula 04 - atividade numpy e matplotlib

Nomes: Roger Rothmund, Patrick Martini, Luís Felipe Schmidt
Analisar vetor e plotar graficos.

'''
import tkinter as tk
import os
import numpy as np
import matplotlib.pyplot as plt

from tkinter.filedialog import askopenfile 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Calcular a média da Coluna
#Calcular o desvio padrão da coluna
#Subtrair cada item da coluna pela média e dividir pelo desvio padrão da coluna


def openFile(): 
    fileArray = []
    file = askopenfile(mode ='r') 
    if file is not None: 
        content = file.readlines()

        fileName = os.path.basename(file.name)
        labelFileName['text'] = fileName

        for line in content:
            arrayLine = line.split(",")
            arrayLine = [float(i) for i in arrayLine]
            fileArray.append(arrayLine)
        
        file.close()

    dataArr = np.array(fileArray)

    mediaCol = np.mean(dataArr, axis=0)
    desvioPadrãoCol = np.std(dataArr, axis=0)

    autoScaleResult = autoScale(dataArr, mediaCol, desvioPadrãoCol)

    createPlot(dataArr, mediaCol, desvioPadrãoCol, autoScaleResult)

def createPlot(dataArr, mediaCol, desvioPadrãoCol, autoScaleResult):
    #Frame Original
    figura = plt.figure(figsize=(10,5), dpi=60)
    grafico = figura.add_subplot(111)
    canva = FigureCanvasTkAgg(figura, mainFrame)
    canva.get_tk_widget().grid(column=0, row=2)

    grafico.plot(dataArr, color="blue")
    grafico.plot(autoScaleResult, color="red")
    grafico.legend(["Dados originais", "Auto Scale"])
    leg = grafico.get_legend()
    leg.legendHandles[0].set_color('blue')
    leg.legendHandles[1].set_color('red')

    #Frame mediaCol, desvioPadrãoCol
    figura2 = plt.figure(figsize=(10,5), dpi=60)
    grafico2 = figura2.add_subplot(111)
    canva2 = FigureCanvasTkAgg(figura2, mainFrame)
    canva2.get_tk_widget().grid(column=0, row=3)

    grafico2.plot(mediaCol)
    grafico2.plot(desvioPadrãoCol)
    grafico2.legend(["Media das Colunas", "Desvio Padrão Colunas"])

def autoScale(dataArr, mediaCol, desvioPadrãoCol):

    colunas = len(dataArr[0])
    linhas = len(dataArr)

    autoScaleResult = np.zeros((linhas, colunas), dtype=np.float64)

    for i in range(linhas):
        for j in range(colunas):

            autoScaleResult[i][j] = (dataArr[i][j] - mediaCol[j]) / desvioPadrãoCol[j]

    return autoScaleResult

window = tk.Tk()
window.title('Aula 04 - análise com Numpy')

mainFrame = tk.Frame(master=window)

orientationText = tk.Label(mainFrame, text="Clique no botão abaixo para selecionar o arquivo que deseja analisar.")
orientationText.grid(column=0, row=0, padx=5, pady=5)

#Frame relacionado ao arquivo
openFrame = tk.Frame(master=mainFrame)
openFrame.grid(column=0, row=1, padx=5, pady=5)

openButton = tk.Button(openFrame, text ='Abrir arquivo', command = lambda:openFile()) 
openButton.grid(column=0, row=0)

labelFileName = tk.Label(openFrame, text="...")
labelFileName.grid(column=1, row=0)

mainFrame.pack(side=tk.TOP)

window.mainloop()
