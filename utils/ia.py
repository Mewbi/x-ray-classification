import cv2
import numpy as np
import tensorflow as tf

from config import *
from tensorflow.keras.models import model_from_json
from tensorflow.keras import layers, optimizers
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

def load(app):

    json_file = open(ia['model_json'], 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights(ia['model_h5'])
    print("Loaded model from disk")
    model.compile(optimizer = tf.keras.optimizers.legacy.RMSprop(0.0001, decay = 1e-6), loss = 'categorical_crossentropy', metrics = ['accuracy'])
    #evaluate = model.evaluate_generator(test_generator, steps = test_generator.n // 4, verbose =1)

    img= cv2.imread('ia/test/1/Normal-1056.png')
    img = cv2.resize(img,(256,256))
    img = img / 255
    img = img.reshape(-1,256,256,3)
    predict = model.predict(img)
    predict = np.argmax(predict)
    
    # prediction.append(predict)
    
    # original.append(0)

    
    # score = accuracy_score(original, prediction)
    # print(classification_report(np.asarray(original), np.asarray(prediction)))
    # print(score)

    app.ia = model