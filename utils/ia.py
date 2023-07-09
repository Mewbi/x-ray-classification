import cv2
import numpy as np
import tensorflow as tf

from config import *
from tensorflow.keras.models import model_from_json
from tensorflow.keras import layers, optimizers

def load(app):
    print("\n[ IA ] - Initializing...\n")

    json_file = open(ia['model_json'], 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    model.load_weights(ia['model_h5'])
    
    model.compile(optimizer = tf.keras.optimizers.legacy.RMSprop(0.0001, decay = 1e-6), loss = 'categorical_crossentropy', metrics = ['accuracy'])

    app.ia = model

    print("\n[ IA ] - Loaded model from disk\n")
    