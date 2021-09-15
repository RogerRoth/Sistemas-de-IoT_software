import tkinter as tk
import os
import string
from tkinter.filedialog import askopenfile 

def openFile(): 
    file = askopenfile(mode ='r') 
    if file is not None: 
        content = file.read() 

        [totalPalavras, totalCaracteresSpace, totalCaracteresNoSpace] = countContent(content)

        textWords.insert(0, totalPalavras)
        textCharsSpace.insert(0, totalCaracteresSpace)
        textCharsNoSpace.insert(0, totalCaracteresNoSpace)

        fileName = os.path.basename(file.name)
        labelFileName['text'] = fileName

def countContent(content):
    totalPalavras = sum([i.strip(string.punctuation).isalpha() for i in content.split()])
    totalCaracteresSpace = len(content) - content.count("\n")
    totalCaracteresNoSpace = len(content) - content.count("\n") - content.count(" ")

    print(len(content))
    print(content.count(" "))
    print(content.count("\n"))

    return totalPalavras, totalCaracteresSpace, totalCaracteresNoSpace


window = tk.Tk()
window.title('Contador de palavras')

mainFrame = tk.Frame(master=window)

orientationText = tk.Label(mainFrame, text="Contador de palavras!\nClique no botão abaixo para selecionar o arquivo que deseja contar as palavras.")
orientationText.grid(column=0, row=0, padx=5, pady=5)

#Frame relacionado ao arquivo
openFrame = tk.Frame(master=mainFrame)
openFrame.grid(column=0, row=1, padx=5, pady=5)

openButton = tk.Button(openFrame, text ='Abrir arquivo', command = lambda:openFile()) 
openButton.grid(column=0, row=0)

labelFileName = tk.Label(openFrame, text="...")
labelFileName.grid(column=1, row=0)

#Frame resultante
resultFrame = tk.Frame(master=mainFrame)
resultFrame.grid(column=0, row=2, padx=5, pady=10)

labelWords = tk.Label(resultFrame, text="Total de palavras:")
labelWords.grid(column=0, row=0)
textWords = tk.Entry(resultFrame)
textWords.grid(column=1, row=0)

labelCharsSpace = tk.Label(resultFrame, text="Total de caracteres (com espaço):")
labelCharsSpace.grid(column=0, row=1)
textCharsSpace = tk.Entry(resultFrame)
textCharsSpace.grid(column=1, row=1)

labelCharsNoSpace = tk.Label(resultFrame, text="Total de caracteres (sem espaço):")
labelCharsNoSpace.grid(column=0, row=2)
textCharsNoSpace = tk.Entry(resultFrame)
textCharsNoSpace.grid(column=1, row=2)

mainFrame.pack(side=tk.TOP)

window.mainloop()