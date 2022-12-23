'''from pickletools import long1
import matplotlib as mt
import matplotlib.pyplot as plt
from tensorflow.python.ops.variables import Variable
from tensorflow.python.framework.ops import Tensor
from tensorflow.python.ops.random_ops import random_shuffle
#from sklearn import train_test_split
import pandas as pd
import numpy as np

class neuralNetTensorflowUtilMain():
    def __init__(self):
        pass 
    def createNeuron(self, x, y, radius):
        neuronCircle = plt.Circle((x, y), radius=radius, fill=False)
        plt.gca().add_patch(neuronCircle)
    def createNewLayer(self, numberOfNeurons, numberOfNeuronsInWidestLayers):
        distanceBetweenNeurons = 1
        natRadius = 2
        numberOfNeurons = []
        self.newNeuronList = []
        for i in enumerate(numberOfNeurons):
            if len(numberOfNeurons) <= 8+numberOfNeuronsInWidestLayers:
                newNeuron = self.createNeuron(i+1, distanceBetweenNeurons, radius=natRadius)
                self.newNeuronList.append(newNeuron)
            else:
                raise Exception('The number of neurons exceeds the natural limit of '+numberOfNeurons+' neurons')
    
    def createGroupOfLayers(self, layers, neuronList):
        neuronList=self.newNeuronList
        if layers is not None:
            if neuronList is not None:
                for nLayers in layers: 
                    for neurons in neuronList:
                        self.createNewLayer(neurons, nLayers)
            else:
                raise Exception('There are no neurons in the neuron list please add some neurons to continue')
        else:
            raise Exception('There are no layers in the layers list please add layers to continue')    

    def createNeuralNetVisual(self, layers, figSizeX=None, neuronList=[None], figSizeY=None, figSize=(None), plotData=None, pdfData=None, filename=None):
        if plotData is None:
            if figSize is not None:
                figSize=(figSizeX, figSizeY)
            
            plotFigure = plt.figure(figsize=figSize)

            newNeuronList=[]
            if neuronList is not None:
                for neuron in neuronList:
                    newNeuron = newNeuronList.append(np.array(neuron))
            else:
                newNeuron = newNeuronList.append(np.array(np.NaN))
            neuronList=newNeuronList

            self.createGroupOfLayers(layers, neuronList)
            
            pltDataFull = plotData.get_data()

            newPlot = plt.plot(layers, neuronList, data=pltDataFull)
            newPlot.show()
        
        elif plotData is not None:
            if figSize is not None:
                figSize=(figSizeX, figSizeY)
            
            plotFigure = plt.figure(figsize=figSize)
            
            pltDataFull = plotData.get_data()
            pltDataX = pltDataFull[1:]
            pltDataY = pltDataFull[:1]

            self.createGroupOfLayers(pltDataX, pltDataY)

            newPlot = plt.plot(pltDataX, pltDataY, data=pltDataFull)
            newPlot.show()
        
        if filename is None:
            savedPlot = plt.savefig('untitled.png')
        elif filename is not None:
            savedPlot = plt.savefig(filename+'.png')

    def createDatasetForData(self, datasetToBeMade):
        datasetList = list(datasetToBeMade)
        dataFrame = pd.DataFrame(datasetList)
    def recordData(self, dataToRecord, filename, Mode=None):
        if dataToRecord is not None:
            if Mode == 'read':
                with open(filename, 'r') as file:
                    file.read(dataToRecord)
            elif Mode == 'write':
                with open(filename,'w') as file:
                    file.write(dataToRecord)
        else:
            raise Exception(dataToRecord+'is not present in the dataToRecordVariable, please add that variable to continue.')
    
    def recursiveIndex(self, index):
        newIndexList=[]
        for index in enumerate(newIndexList):
            if newIndexList is not None:
                newIndexList.append(self.recursiveIndex(index))
            else:
                newIndexList.append(newIndexList[index])
            

    def convToVar(self, varToConvList=[]):
        for var in varToConvList:
            if var is not None:
                Variable(var)
            elif var is None:
                varToConvList.append(var)
            else:
                raise Exception(var+' does not exist, please use another variable and try again.')
    
    def convToTensor(self, valueIndex, tenToConvList=[]):
        for tenToConv in tenToConvList:
            if tenToConv is not None:
                if tenToConv == float:
                    return Tensor(tenToConv, valueIndex, dtype=float)
                elif tenToConv == int:
                    return Tensor(tenToConv, valueIndex, dtype=int)
            elif tenToConv is None:
                tenToConvList.append(tenToConv)
            else:
                raise Exception(tenToConv+' does not exist, please use another variable ands try again.')

    def convToNumpyArray(self, arrayList=[]):
        for array in arrayList:
            if array is not None:
                if array == float:
                    return np.array(array, float)
                elif array == int:
                    return np.array(array, int)
            elif arrayList is None:
                arrayList.append(array)
            else:
                raise Exception(array+' does not exist, please use another variable ands try again.')
    
    def convToBool(self, boolToConv):
        newBool = bool(boolToConv)
        return newBool

    def recursiveLoader(self, object, x, y, batchSize):
        length = int(len(y) / batchSize)
        indexList = random_shuffle(len(y))
        def iterate(self):
            self.currentIter = 0
            return self
        
        def nextIter(self):
            if self.current < self.length:
                index = indexList[self.current * self.batchSize: (self.current + 1) * self.batchSize]
                self.current += 1
                return self.recursiveIndex((self.X, self.y), index)
    
    def convToVarRecurred(self, item, valueIndex=None, type=None):
        if item is dict:
            return {self.convToVarRecurred(value, type=type) for value in item.items()}
        if item is tuple:
            return {self.convToVarRecurred(element, type=type) for element in item.items()}
        else:
            try:
                if type is long1:
                    return Tensor(item, valueIndex, dtype=long1)
                elif type is float:
                    return Tensor(item, valueIndex, dtype=float)
                elif type is bool:
                    return Tensor(item, valueIndex, dtype=bool)
            except:
                return [self.convToVarRecurred(element, type=type) for element in item]



    def plotNetwork(self, layers, figSizeX=None, neuronList=[None], figSizeY=None, figSize=(None), plotData=None, pdfData=None):
        self.createNeuralNetVisual(layers, figSizeX, neuronList, figSizeY, figSize, plotData, pdfData)
            

    def applyOccomsRazor(self, numberToOccom):
        if numberToOccom is float:
            return np.round(numberToOccom)
        else:
            raise Exception('There are currently no numbers to use occoms razer on, please enter a decimal')'''
    
    


    