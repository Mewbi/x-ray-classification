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

    def __init__(self, 
                file_bin,
                user_id,
                username,
                age,
                name,
                date): 
        self.image = file_bin 
        self.hash = self.image
        self.user_id = user_id 
        self.username = username
        self.age = age
        self.name = name
        self.date = date
        self.result = ""

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
    def image(self, file_bin):
        img = cv2.imdecode(np.fromstring(file_bin, np.uint8), cv2.IMREAD_COLOR)
        img = cv2.resize(img, (256,256))
        img = img / 255
        img = img.reshape(-1,256,256,3)
        self._image = img
        self._image_raw = file_bin

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    @property
    def image_raw(self):
        return self._image_raw

    @image_raw.setter
    def image_raw(self, value):
        self._image_raw = value


    def classify(self):
        prediction = self.APP.ia.predict(self.image)
        prediction = np.argmax(prediction)
        return self.CLASSIFICATIONS[prediction]

    def report(self):
        return {
            "hash": self.hash,
            "classification": self.classify()
        }