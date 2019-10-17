# -*- coding: utf-8 -*-
"""TF-Coursera-Week-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vqw_WguUMt_BhMOi3l3cmcH4QRCN2Z7x
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

# create the data object and load the data
# into train and test images and labels

data = keras.datasets.fashion_mnist
(images_train, labels_train), (images_test, labels_test) = data.load_data()

# explore the data
import matplotlib.pyplot as plt

# explore the shape and dimension of the images
print("train images shape", images_train.shape)
print("number of train images", images_train.shape[0])
print("number of test images", images_test.shape[0])
print("shape of images", images_train.shape[1:])

# assert the test and train data to have the same shape
assert images_test.shape[1:] == images_train.shape[1:]

# explore the labels
print("train labels shape", labels_train.shape)
print("a few sample labels", labels_train[1:11])
print("minimum value of labels", min(labels_test))
print("maximum value of labels", max(labels_test))
print(images_train.dtype)
print(labels_train.dtype)

# set the class name in English
# get from https://github.com/zalandoresearch/fashion-mnist
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# show some label and images
# visualize the data

# randomly visualize n images in training data
no_samples = 4
plt.figure(figsize=(10,10))
for i in range(no_samples):
  idx = np.random.randint(0, images_train.shape[0])
  plt.subplot(1,no_samples,i+1)
  plt.xticks([])
  plt.yticks([])
  plt.imshow(images_train[idx], cmap=plt.cm.binary)
  plt.xlabel(class_names[labels_train[idx]])
plt.show()

# normalize the data
images_train  = images_train / 255.0
images_test = images_test / 255.0

# create a model to do the prediction
# flatten layer of 28*28 = 784
# first hidden layer: 128 
# second hidden layer: 60
# last layer: softmax of size of len of labels.
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(units=128, activation=tf.nn.relu),
    keras.layers.Dense(units=60, activation=tf.nn.relu),
    keras.layers.Dense(units=10, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.optimizers.Adam(), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x=images_train, y=labels_train, epochs=10)

model.evaluate(images_test, labels_test)

# get the classification results
predictions = model.predict(images_test)
print(np.argmax(predictions[0]))

# visualize the predictions
no_samples = 5
plt.figure(figsize=(10,10))
for i in range(no_samples):
  idx = np.random.randint(0, images_test.shape[0])
  plt.subplot(1,no_samples,i+1)
  plt.xticks([])
  plt.yticks([])
  plt.imshow(images_test[idx], cmap=plt.cm.binary)
  plt.xlabel("Target: " + class_names[labels_test[idx]]
             + "\n predicted:" + class_names[np.argmax(predictions[idx])] )
plt.show()

# How to set-up callbacks

import tensorflow as tf

class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('accuracy')>0.6):
      print("\nReached 60% accuracy so cancelling training!")
      self.model.stop_training = True

mnist = tf.keras.datasets.fashion_mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

callbacks = myCallback()

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, callbacks=[callbacks])

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if logs.get('accuracy') > 0.997:
            print("\the trainign reached 99% percent accuracy!")
            self.model.stop_training = True
     
# train_mnist
def train_mnist():
    # load mnist dataset
    mnist = tf.keras.datasets.mnist
    (x_train, y_train),(x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    
    callbacks = myCallback()
    
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(512, activation=tf.nn.relu),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ])
    
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    # model fitting
    history = model.fit(x_train, y_train, epochs=10, callbacks=[callbacks])
    # model fitting
    return history.epoch, history.history['accuracy'][-1]

train_mnist()