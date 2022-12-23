from numbers import Number
from pickletools import optimize
from re import X
from turtle import shape
from sklearn import metrics
import tensorflow as tf
import numpy as np 
from tensorflow.python.keras import layers
from tensorflow.python.keras.layers import Activation, Dense, Dropout
from tensorflow.python.ops.variables import Variable
from keras.models import Sequential
import matplotlib
from sklearn.model_selection import train_test_split
from tensorflow.python import keras
import matplotlib.pyplot as plt
from tensorflow.python.ops.linalg_ops import norm
import wolframalpha as wolf
from os import path, read
import autograd
import sys
import pandas as pd
import re
from tqdm import tqdm, trange
from tensorflow.python.keras.losses import MeanSquaredError






class NetMain():
    def __init__(self):
        self.InitializeNeuralNet()
    def conv_x_to_var(self, x):
        return Variable(np.array(x), (len(x), len(x)), dtype=float)
    def conv_y_to_var(self, y):
        return Variable(np.array(y), (len(y), len(y)), dtype=float)
    def conv_to_numpy(self, n):
        return np.ndarray(n)
    def train(self, X=None, y=None, train_loader=None, validation_data=None, validation_loader=None, criterion=MeanSquaredError(), inspect_interval = 10, isPlotted=False, is_cuda=None, epochs=300, Nsamples=20000, max_Nfeatures=100, **kwargs):       
        def get_regularization(model, loss_epoch, **kwargs):
            reg_dict = kwargs["reg_dict"] if "reg_dict" in kwargs else None
            reg = self.conv_x_to_var([0])
            if reg_dict is not None:
                for reg_type, reg_coeff in reg_dict.items():
                    if isinstance(reg_coeff, Number):
                        reg_coeff_ele = reg_coeff
                    else:
                        if loss_epoch < len(reg_coeff):
                            reg_coeff_ele = reg_coeff[loss_epoch]
                        else:
                            reg_coeff_ele = reg_coeff[-1]
                    reg = reg + model.get
        #vegaMain = VegaAiMain()
        Xs = []
        ys = []
        #Xs.append(vegaMain.first_answer)
        #ys.append(vegaMain.second_answer)
        for isample in trange(Nsamples):
            Nfeatures = np.random.randint(max_Nfeatures-40)+40

            intermediateX = np.random.rand(Nfeatures, 3) * 50 - 50 * np.random.rand(3)

            X = np.zeros((Nfeatures, Nfeatures, 6))
            X[:,:,:3] = np.expand_dims(intermediateX, 1)
            X[:,:,3:] = np.expand_dims(intermediateX, 0)
            X = X.reshape(-1,6)
            X = X * np.mgrid[1:2:len(X)]   # a modification that would seem meaningless from your point of view... just keep it...
            # Note: all these is similar to below; but I found my data-generating method to generate much-harder-to-train data
            # X = np.random.rand(Nfeatures * Nfeatures, 6)

            # generate y
            origin = self.conv_x_to_var([0,0,0])
            # firstly, z=f(x)
            X1 = self.conv_x_to_var(X[:,:3]) - origin   # example shape: (2500, 3); origin=0 so ignore origin for now
            X2 = self.conv_x_to_var(X[:,3:]) - origin
            R1 = tf.norm(X1)       # example shape: (2500, 1)
            R2 = tf.norm(X2)
            z = 1 / R1 / R2      # example shape: (2500, 1)
            z = tf.math.reduce_sum(z) * 1e4        # example shape: 1
            # then y=g(z). why not just ask you to train z? because training y is much more difficult than z.
            with tf.GradientTape() as g:
                y = self.conv_to_numpy(g.gradient(z, origin))
            

            Xs.append(np.mean(X, 0))
            ys.append(y / (len(X)))


        print("\n")
        print(Xs[0].shape)
        print(y.shape)
        print(y)
        print(X[0])
        print(Xs[0])
        print(ys[0])


        X_train, X_test, y_train, y_test = train_test_split(Xs, ys, train_size = 0.8)
        print(type(X_train))

        print("train")
        print(len(X_train))
        print(X_train[0].shape)
        model = Sequential()
        model.add(Dense(units=400, input_dim=6))
        model.add(Activation('relu'))
        model.add(Dense(units=200))
        model.add(Activation('relu'))
        model.add(Dense(units=100))
        model.add(Dropout(0.2))
        model.add(Activation('relu'))
        model.add(Dropout(0.2))
        model.add(Dense(units=50))
        model.add(Activation('relu'))
        model.add(Dropout(0.2))
        model.add(Dense(units=25))
        model.add(Activation('relu'))
        model.add(Dense(units=3))

        sgd = tf.keras.optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='mean_squared_error',
                    optimizer='sgd',metrics=['accuracy'])

        model.fit(np.array(X_train), np.array(y_train), epochs=100, batch_size=50, verbose=2)

        loss_and_metrics = model.evaluate(np.array(X_test), np.array(y_test), batch_size=100)

        classes = model.predict(np.array(X_test), batch_size=1)

        print(classes[:10])
        print(y_test[:10])
        '''X = np.array((self.conv_x_to_var(vegaMain.first_answer), [0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]), dtype=float)
 
        y = np.array(([1], [0], [0], [0], [0], [0], [0], [1]), dtype=float)
        
        model = tf.keras.Sequential()

        model.add(Dense(4, input_dim=3, activation=activation, use_bias=True))

        model.compile(loss=loss, optimizer=optimizer, metrics=metrics)

        #print(model.get_weights())

        history = model.fit(X, y, epochs=epochs, validation_data=(X, y))

        model.summary()

        loss_history = history.history["loss"]
        numpy_loss_history = np.array(loss_history)
        np.savetxt('loss_history.txt', numpy_loss_history, delimiter="\n")

        binary_accuracy_history = history.history["binary_accuracy"]
        numpy_binary_accuracy = np.array(binary_accuracy_history)
        np.savetxt("binary_accuracy.txt", numpy_binary_accuracy, delimiter="\n")

        print(np.mean(history.history["binary_accuracy"]))

        result = model.predict(X).round()

        print(result)'''    
net = NetMain()




