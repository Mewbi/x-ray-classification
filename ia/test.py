#!/usr/bin/env python3

import os
import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from sklearn.metrics import classification_report, accuracy_score


# Setup Vars
model_json_path = "model/model.json"
model_path = "model/model.h5"
test_directory = "test"
label_names = {
        0: "Covid-19", 
        1: "Normal", 
        2: "Lung opacity", 
        3: "Viral Pneumonia"
}


# Load Model
print("Loading model from disk...")

json_file = open(model_json_path, "r")
loaded_model_json = json_file.read()
json_file.close()

model = model_from_json(loaded_model_json)
model.load_weights(model_path)


# Compile model
print("Compiling model...")

model.compile(optimizer = tf.keras.optimizers.legacy.RMSprop(0.0001, decay = 1e-6), 
              loss = "categorical_crossentropy", 
              metrics = ["accuracy"])


# Prepare test
test_gen = ImageDataGenerator(rescale = 1./255)
test_generator = test_gen.flow_from_directory(batch_size = 4, 
                                              directory = test_directory, 
                                              shuffle = True, 
                                              target_size=(256,256), 
                                              class_mode= 'categorical')


# Test accuracy
print("Testing accuracy...")

evaluate = model.evaluate_generator(test_generator, steps = test_generator.n // 4, verbose =1)

print("Accuracy Test: {}".format(evaluate[1]))

prediction = []
original = []
image = []


# Test images
print("Testing images...")

for i in range(len(os.listdir(test_directory))):
  for item in os.listdir(os.path.join(test_directory,str(i))):
    img= cv2.imread(os.path.join(test_directory,str(i),item))
    img = cv2.resize(img,(256,256))
    image.append(img)
    img = img / 255
    img = img.reshape(-1,256,256,3)
    predict = model.predict(img)
    predict = np.argmax(predict)
    prediction.append(predict)
    original.append(i)


score = accuracy_score(original, prediction)
print("Test Accuracy : {}".format(score))


# Plot results
print("Plotting results...")
L = 5
W = 5

fig, axes = plt.subplots(L, W, figsize = (12, 12))
axes = axes.ravel()

for i in np.arange(0, L*W):
    axes[i].imshow(image[i])
    axes[i].set_title('Guess={}\nTrue={}'.format(str(label_names[prediction[i]]), str(label_names[original[i]])))
    axes[i].axis('off')

plt.subplots_adjust(wspace = 1.2)

print(classification_report(np.asarray(original), np.asarray(prediction)))

plt.show()
