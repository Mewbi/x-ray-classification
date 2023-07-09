import cv2
import hashlib
import numpy as np

from flask import current_app

class Image():

    APP = current_app
    CLASSIFICATIONS = {
        0: 'Covid-19', 
        1: 'Normal', 
        2: 'Lung opacity', 
        3: 'Viral Pneumonia'
    }

    def __init__(self, filename):
        self.image = filename
        self.hash = self.image

    @property
    def hash(self):
        return self._hash

    @hash.setter
    def hash(self, image):
        self._hash = hashlib.md5(image).hexdigest()

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, filename):
        img = cv2.imdecode(np.fromstring(filename.read(), np.uint8), cv2.IMREAD_COLOR)
        img = cv2.resize(img, (256,256))
        img = img / 255
        img = img.reshape(-1,256,256,3)
        self._image = img
    
    def classify(self):
        prediction = self.APP.ia.predict(self.image)
        prediction = np.argmax(prediction)
        return self.CLASSIFICATIONS[prediction]

    def report(self):
        return {
            "hash": self.hash,
            "classification": self.classify()
        }