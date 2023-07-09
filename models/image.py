import cv2
import numpy as np

from flask import current_app

class Image():

    app = current_app

    def __init__(self, filename):
        self.image = filename

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
        return self.app.ia.predict(self.image)