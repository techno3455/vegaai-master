'''from operator import index
import tkinter as ttk
import tkinter as tk
import wikipedia 
import random
import wolframalpha
from gtts import gTTS
import playsound
import speech_recognition as sr
import matplotlib.pyplot as plt
import scipy as sci
import numpy as np
import nltk as nl
import pandas as pd
import os
import random
import pyttsx3
import serial as ps
import time
from tkinter import *
import utilities.neuralnet_util as util
import fileinput
class person:
    name = ''
    def setName(self, name):
        self.name = name

class VegaMain:
    def __init__(self):
        super().__init__()
        self.firstVarAnswer = None
        self.secondVarAnswer = None
        self.language = 'en-us'
        #self.initSerialComm()
    def thereExists(self, terms):
        for term in terms:
            if term in self.query:
                return True

    def VegaTakeCommand(self, ask=False):
     
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            if ask:
                self.VegaSpeak(ask)
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
    
        try:
            print("Recognizing...")   
            self.query = r.recognize_google(audio, language=self.language)
            print(f"User said: {self.query}\n")
        except Exception as e:
            print(e)   
            print("Unable to Recognize your voice.") 
            return "None"
        
        return self.query

    def VegaSpeak(self, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()


    

    

    # sample code, to split all script input files into paragraphs
    def searchData(self, voiceData, firstVarAnswer, secondVarAnswer):
        debug = True
        if debug is not True:
            self.conversionList = {'sign':'sine', 'Cam':'Com', 'cam':'com', 'Tom':'Com', 'Ford':'4', 'Bomb':'Com', 'Force':'4', 'cosign':'cosine', 'some':'sum', 'pie':'pi', 'won':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'ate':'8', 'nine':'9', 'zero':'0', 'plus':'+', 'minus':'-', 'times':'*', 'divide':'/', 'calcul8':'calculate'}
            self.queryConversionList = {'sine':np.sin, 'cosine':np.cos, 'tangent':np.tan, 'logarithim':np.log, 'mod':np.mod, 'sqaure root':np.sqrt}
            for word in self.conversionList.keys():
                self.query = self.query.replace(word, self.conversionList.get(word))
                print(self.query)
            if self.thereExists(['get']):
                client = wolframalpha.Client('5X2A65-4WYGVPQ6AV')
                res1 = client.query(self.query.lower())
                self.firstVarAnswer = next(res1.results).text
                self.VegaSpeak(self.firstVarAnswer)
                voiceData = self.VegaTakeCommand('What is your second variable?')
                choice = voiceData
                if 'get' in choice.lower():
                    res2 = client.query(self.query.lower())
                    self.secondVarAnswer = next(res2.results).text
                    self.VegaSpeak(self.secondVarAnswer)

            if self.thereExists(["what"]):
                client = wolframalpha.Client('5X2A65-4WYGVPQ6AV')
                res = client.query(self.query.lower())
                firstAnswer = next(res.results).text
                print(firstAnswer)
                self.VegaSpeak(firstAnswer)
                self.questionFormat = voiceData[int(len(voiceData)/2):]
                voiceData = self.VegaTakeCommand('Would you like to know more about ' + self.questionFormat + '?')
                choice = voiceData
                if "yes" or "sure" or "fine" or "yea" in choice.lower():
                    for pod in res.pods:
                        print('title:', pod.title)
                        for sub in pod.subpods:
                            self.postString = sub.plaintext.split("\n",1)[0]
                            #print(self.postString)
                            #self.VegaSpeak(self.postString)
                
                            self.filename = 'vegadata.txt'
                            with open(self.filename, 'w', encoding="utf-8") as f:
                                f.write(str(sub.plaintext))
                    print('\n---\n')
                    print('title:', pod.title)
                    self.VegaSpeak('Alright, here is some more information about ' + self.questionFormat)
                    self.VegaSpeak(sub.plaintext)
                    time.sleep(1.0)
                    voiceData = self.VegaTakeCommand('Would you like me to include ' + self.questionFormat + ' in your experiment?')
                    choice = voiceData
                    if "yes" or "sure" or "fine" or "yea" in choice.lower():
                        voiceData = self.VegaTakeCommand('Alright, what would you like to name your experiment?')
                        choice = voiceData
                        if "name" or "name it" or "title it" in choice():
                            choice = voiceData
                            self.searchTitle = choice.split("name")[-1]
                            self.searchTitle = choice.split("title")[-1]
                            self.searchTitle = choice.split("it")[-1]
                            with open('arduinoData.txt', 'w', encoding='utf-8') as f:
                                f.write('Varaibles for ai recognition: \n ---------------------------------- \n')
                                f.write(self.postString)
                            voiceData = self.VegaTakeCommand('Alright, what is your com port name?')
                            choice = voiceData
                            if "it's" or "it is" or "name" or "named" in choice():
                                searchCom = choice.split("its")[-1]
                                searchCom = choice.split("it is")[-1]
                                searchCom = choice.split("name")[-1] 
                                searchCom = choice.split("named")[-1]
                                #for word in str(self.conversionList.keys()):
                                    #self.newPortName = searchCom.replace(word, str(self.conversionList.get(word)))
                                    #self.newPortName.replace('Cam', str(self.conversionList.get('Cam')))
                                    #self.newPortName.replace(str(" ", ".", "?", "!", ","), "")
                                    
                                    
                                #arduino = ps.Serial(self.newPortName, '9600')
                                #arduinoData = arduino.readline()
                                #decodedValues = str(arduinoData[0:len(arduinoData)].decode('utf-8'))
                                #print(decodedValues)
                                with open(f'{self.searchTitle}.txt', 'w') as f:
                                    f.write('\n Arduino Code and Varaibles for ai recognition: \n ---------------------------------- \n')
                                    #f.write(decodedValues)
                                    #data = {'one':pd.Series(['1.', '2.', '.3', '4.'], index=['a', 'b', 'c', 'd']),'two':pd.Series([self.postString, decodedValues], index=['a', 'b', 'c', 'd'])}
                                    #dataFrame = pd.DataFrame(data)

                                    #dataFrameWithDummyData = pd.get_dummies(dataFrame, columns=["two"], drop_first=False)
                                    #print(dataFrameWithDummyData)
                                    
                                    ## create a dataframe for the theory so it can be processed through the theoryHub function.
                                    with open(self.filename, 'r') as f:
                                        dataread = f.read()
                                        self.subData = {'one':pd.Series([1], index=['a']), 'two':pd.Series([dataread], index=['a'])}
                                        self.subData['new_column'] = pd.Series(firstAnswer)
                                        self.subDataFrame = pd.DataFrame(self.subData)
                                        

                                        self.subDataFrameWithDummyData = pd.get_dummies(self.subDataFrame, columns=['two'], drop_first=False)
                                        print(self.subDataFrameWithDummyData)

                                    ## assemble a theory so we can give the user what they want.
                                    util.theoryHub(self.subDataFrameWithDummyData, 'leakyRelu', None)
                                        

                            elif "no" or "no thanks" or "nope" or "no thank" in choice.lower():
                                self.VegaSpeak('Alright I will go back to the dashboard, if you need me just give me a call.')
                                return
                        elif "no" or "no thanks" or "nope" or "no thank" in choice.lower():
                            self.VegaSpeak('Alright I will go back to the dashboard, if you need me just give me a call.')
                            return
                    elif "no" or "no thanks" or "nope" or "no thank" in choice.lower():
                        self.VegaSpeak('Alright I will go back to the dashboard, if you need me just give me a call.')
                        return                
                elif "no" or "no thanks" or "nope" or "no thank" in choice.lower():
                    self.VegaSpeak('Alright I will go back to the dashboard, if you need me just give me a call.')
                    return
        if debug:
            self.filename = 'vegadata.txt'
            with open(self.filename, 'r') as f:
                dataread = f.read()
                self.subData = {'one':pd.Series([1], index=['a']), 'two':pd.Series([dataread], index=['a'])}
                self.subData['new_column'] = pd.Series(voiceData)
                self.subDataFrame = pd.DataFrame(self.subData)
                

                self.subDataFrameWithDummyData = pd.get_dummies(self.subDataFrame, columns=['two'], drop_first=False)
                print(self.subDataFrameWithDummyData)

            ## assemble a theory so we can give the user what they want.
            util.theoryHub(self.subDataFrameWithDummyData, 'leakyRelu', None)
            

            self.VegaSpeak('Would you like me to cross reference ' + firstAnswer + 'to' + sub.plaintext + '?')
            print('Would you like me to cross reference ' + firstAnswer + ' to ' + sub.plaintext + '?')
                if self.thereExists("yes"):
                    res2 = client.query(self.query.lower())
                    secondAnswer = next(res2.results).text
                    for pod in res2.pods:
                        print('title:', pod.title)
                        for sub in pod.subpods:
                            print(sub.plaintext)
                            with open(self.filename, 'w') as f:
                                f.write(secondAnswer)
                                f.write(str(sub.plaintext))
                                with open(self.filename, 'r') as f:
                                    #answerTokens = nl.word_tokenize(str(sub.plaintext))
                                    #textPart1 = nl.Text(answerTokens)
                                    #print(textPart1)
                                    self.VegaSpeak(str(sub.plaintext))
                                    self.VegaSpeak('are you using ' + firstAnswer + ' in your experiment?')
                                    if self.thereExists("yes"):
                                        self.VegaSpeak('ok, would you like me to use ' + firstAnswer + 'in your experiment if it is applicable?')
                                        if self.thereExists("yes"):
                                            self.VegaSpeak('Alright sounds good, let me just connect to your device and read the devices ports!')
                                            listInFloats = []
                                            listVals = []
                                            arduino = ps.Serial('com4', 9600)
                                            print('Established serial connection to Arduino')
                                            arduinoData = arduino.readline()
                                            decodedVals = str(arduinoData[0:len(arduinoData)].decode('utf-8'))
                                            listVals = decodedVals.split('x')

                                            for item in listVals:
                                                listInFloats.append(float(item))

                                            print(f'Collected readings from Arduino: {listInFloats}')
                                            
                                            arduinoData = 0
                                            listInFloats.clear()
                                            listVals.clear()
                                            arduino.close()
                                            print('Connection closed')
                                            print('<----------------------------->')

                                            else:
                                                self.VegaSpeak('Alright I will go back to the mainboard if you need me just press the button in the network tab.')
                                        else:
                                            self.VegaSpeak('Alrighty then, I will go back to the mainboard if you need me just ask.')
        #if self.thereExists(["my name is"]).lower():
            #personName = self.query.split("is")[-1].strip()
            #self.VegaSpeak(f'okay, i will remember your name {personName}')
            #self.personObj = person()
            #self.personObj.setName(personName)
        
        if self.thereExists(["what is your name","what's your name","tell me your name"]):
            if self.personObj.name:
                self.VegaSpeak('My name is Vega and I am here to help you with your research.')
            else:
                self.VegaSpeak('My name is Vega and I am here to help you with your research.')
                self.VegaSpeak('May I ask what your name is?')

        if self.thereExists(["calculate"]):
            client = wolframalpha.Client('5X2A65-4WYGVPQ6AV')
            indx = self.query.lower().split().index('calculate')
            print('hello?')
            query = self.query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            self.VegaSpeak("The answer is " + answer)
            for word in self.queryConversionList.keys():
                function = self.query.find(word)
                function = self.queryConversionList.get(word)
            

            self.VegaCreatePlot2D(self.queryConversionList, function)
            for pod in res.pods:
                print('title:', pod.title)
                for sub in pod.subpods:
                    print(sub.plaintext)
                    self.filename = 'vegadata.csv'
                    with open(self.filename, 'w') as f:
                        f.write(answer)
                        f.write(str(sub.plaintext))
                #print('\n---\n')
        
        def VegaCreatePlot2D(self, namelist=None ,function=None, x=np.linspace(-2*np.pi, 2*np.pi, 1000)):
            self.y = function(x)
            name = 'whitespace'
            for word in namelist.keys():
                if namelist.get(word) == function:
                    name = word
            ax1 = plt.subplot(1, 1, 1)
            ax1.margins(0.05, 2)
            ax1.plot(x, self.y)
            plt.text(np.median(x), np.max(self.y)+2, name)
            plt.show()
        
        def VegaCreatePlot3D(self, namelist=None, function=None, x=np.linspace(-2*np.pi, 2*np.pi, 1000)):
            name = 'whitespace'
            for word in namelist.keys():
                if namelist.get(word) == function:
                    name = word
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            x = y = np.arange(-3.0, 3.0, 0.05)
            X, Y = np.meshgrid(x, y)
            zs = np.array(function(np.ravel(X), np.ravel(Y)))
            Z = zs.reshape(X.shape)

            ax.plot_surface(X, Y, Z)

            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_zlabel('Z Label')

            plt.show()
        
        #def CreateDownwardsParaboloid(self, x, y):
            #return x**2 + y**2
        
        #def CreateUpwardsParaboloid(self, x, y):
            #return -x**2 + -y**2
        
                    
        #def convertPhysicalOperation(self, mathOperation):
            
            
        def storeInformation(self, information):
            filename = 'infoDat.db'
            f = open(filename, "w")
            f.write(information)
            f.close()

            f = open(filename, "r")
            print(f.read())
            f.close()

        def readInformation(self, information):
            filename = 'infoDat.db'
            f = open(filename, 'w')
            f.read(information)
            
            print(f.read())
            f.close()   
                
        def initSerialComm(self):
            arduino = ps.Serial(port='COM5', baudrate=9600, timeout=.1)
            def WriteRead(x):
                arduino.write(bytes(x, 'utf-8'))
                time.sleep(0.05)
                self.data = arduino.readline()
                return self.data
            while True:
                num = input('Enter a number: ')
                value = WriteRead(num)
                print(value)
            arduino.close()


    



def main():
    root = tk.Tk()
    app = VegaMain()
    debug = False
    while(1):
        if debug is not True:
            voiceData = app.VegaTakeCommand()
            app.searchData(voiceData)
        if debug:
            print('**************Debug for Vega 1.0**************')
            print('Made by: Trevor Blanchard, Copyright (C) TetraSystemSolutions 2021')
            debugInput = input('What is the main answer that you would like to test?')
            app.searchData(debugInput)   


if __name__ == '__main__':
    main()'''


    