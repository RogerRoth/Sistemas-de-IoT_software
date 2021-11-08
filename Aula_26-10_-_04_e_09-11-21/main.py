
import os
import pandas as pd 

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def openTrainingSet(fileName) :
    trainingSet = pd.read_csv(os.path.join(__location__, 'data', fileName))

    return trainingSet

def datasetTreatment():
    
    dataSet = openTrainingSet('nir.csv')

    #Tratamento dos dados

    dataSet.drop(['Sample'], axis = 1, inplace=True)

    print(dataSet)
    return(dataSet)


import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import LeaveOneOut, cross_val_predict, KFold
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram
from sklearn.cluster import AgglomerativeClustering
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model
import joblib
import warnings

warnings.filterwarnings('ignore')

def plot(x,y):
    with plt.style.context(('ggplot')):
        plt.plot(x,y)
        plt.xlabel(u'Wavelength')
        plt.ylabel(u'Intensisty')
        plt.title(u'Spectra chart')
        plt.show()
		
def scatter(scores, classes):
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
        plt.title('Principal Component Analysis')
    plt.show()

def snv(input_data):          
    # Define a new array and populate it with the corrected data        
    output_data = np.zeros_like(input_data)      
    for i in range(input_data.shape[0]):            
        # Apply correction          
        output_data[i,:] = (input_data[i,:] - np.mean(input_data[i,:])) / np.std(input_data[i,:])        
    return output_data
	
#df = pd.read_csv("nir.csv")
df = openTrainingSet('nir.csv')


#sys.exit()

wave = df.iloc[1:,0].to_numpy()


#sys.exit()
data = df.iloc[1:,1:].to_numpy().T


classes = df.iloc[0,1:].to_numpy()


plot(wave,data.T)

#sys.exit()

#não-supervisionado
print('PCA')
pca = PCA(n_components=3)
scores = pca.fit_transform(data)
scatter(scores, classes)

data = data[:,2857:2909]
pca = PCA(n_components=4)
data = savgol_filter(snv(data), 5, polyorder = 2, deriv=1)
scores = pca.fit_transform(data)
scatter(scores, classes)
