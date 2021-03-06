# -*- coding: utf-8 -*-
"""TF-Coursera-Week-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GXHm-ICWyFYqRl3F5B-dRjwUZpDKgAk7
"""

# sanity check for the tensorflowversion of Colab
# import tensorflow as tf
# print(tf.__version__)

# Upgrade to TF 2
# please not that you need to reset the 
# runtimes before importing the new tf
!pip install tensorflow==2.0.0-alpha0

import tensorflow as tf
print(tf.__version__)

# import the keras api inside the tf
import tensorflow.keras as keras
import numpy as np

# create a model to predict the pattern rule for translating xs to ys
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# use one node with sigmoid function to perform the prediction of rule
# define the model
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# define the loss and compile method
model.compile(optimizer='sgd', loss='mean_squared_error')
# train
model.fit(xs, ys, epochs=600, verbose=0)

# predict the future value
print(model.predict([10.0]))

import tensorflow as tf
import numpy as np
from tensorflow import keras

# house_model
def house_model(y_new):
    xs = np.random.random(100) 
    ys = 0.5 * xs + 0.5 
    # print(xs)
    # print(ys)
    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])]) 
    model.compile(optimizer='sgd', loss='mean_squared_error')
    model.fit(xs, ys, epochs=3000)
    return model.predict(y_new)[0]

prediction = house_model([7.0])
print(prediction)