import os
import pandas as pd 
import sys
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import warnings
from math import floor
import getopt

warnings.filterwarnings('ignore')

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def openTrainingSet(fileName) :
    trainingSet = pd.read_csv(os.path.join(__location__, 'data', fileName))

    return trainingSet

def calculateInterval(filePath, interval):
    df = pd.read_csv(filePath)

    intervalSize = floor((len(df)-1)/interval)

    classes = df.iloc[0, 1:].to_numpy()
    data = df.iloc[1:, 1:].to_numpy().T

    for i in range(interval):
        if i == 0:
            init = i * intervalSize
        else:
            init = i * intervalSize + 1
        if i == interval - 1:
            final = len(data[0])
        else:
            final = init + intervalSize
        dataAux = data[:, init:final]

        pca = PCA(n_components=3)
        scores = pca.fit_transform(dataAux)
        titleAux = f'[{init} - {final}]'
        scatter(scores, classes, titleAux)

		
def scatter(scores, classes, title):
    unique = list(set(classes))
    colors = [plt.cm.jet(float(i)/max(unique)) for i in unique]
    with plt.style.context(('ggplot')):
        for i, u in enumerate(unique):
            xi = [scores[j,0] for j  in range(len(scores[:,0])) if classes[j] == u]
            yi = [scores[j,1] for j  in range(len(scores[:,1])) if classes[j] == u]
            plt.scatter(xi, yi, c=colors[i], s=60, edgecolors='k',label=str(u))

        plt.xlabel('PC1')
        plt.ylabel('PC2')
        #plt.legend(labplot,loc='lower right')
        plt.title(f'Principal Component Analysis - {title}')
    plt.show()

filepath = ''
interval = ''
argv = sys.argv[1:]

try:
    options, args = getopt.getopt(argv, 'f:i:', ['file =', 'interval ='])

except:
    print('Incorrect parameters')

for name, value in options:
    if name in ['-f', '--file']:
        filePath = value
    elif name in ['-i', '--interval']:
        interval = value

calculateInterval(filePath, int(interval))

#& C:/Python39/python.exe "f:/Roger/Faculdade/Sistemas de IoT/Software/Aula_26-10_-_04_e_09-11-21/main.py" -f 'Aula_26-10_-_04_e_09-11-21/data/nir.csv' -i 3