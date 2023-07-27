#!/usr/bin/env python3

import os
import numpy as np
import tensorflow as tf
from tensorflow.python.client import device_lib
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras import layers, optimizers
from tensorflow.keras.layers import Input, Add, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D, AveragePooling2D, MaxPooling2D, Dropout
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import backend as K
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint, LearningRateScheduler
import matplotlib.pyplot as plt


from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import cv2

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
device_lib.list_local_devices()

os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

# labels Translator 
label_names = {0 : 'Covid-19', 1 : 'Normal' , 2: 'Lung opacity', 3 : 'Viral Pneumonia'}

# XRay_Directory = 'train'
# os.listdir(XRay_Directory)


# # Use image generator to generate tensor images data and normalize them
# # Use 20% of the data for cross-validation
# image_generator = ImageDataGenerator(rescale = 1./255, validation_split = 0.2)

# # Generate batches of 40 images
# # Total number of images is 133*4 = 532 images
# # Training is 428 (80%) and validation is 104 (20%)
# # Perform shuffling and image resizing

# train_generator = image_generator.flow_from_directory(batch_size = 40,
#                                                      directory = XRay_Directory,
#                                                      shuffle =  True,
#                                                      target_size = (256, 256),
#                                                      class_mode = 'categorical',
#                                                      subset = 'training')



# validation_generator = image_generator.flow_from_directory(batch_size = 40,
#                                                            directory = XRay_Directory, 
#                                                            shuffle = True, 
#                                                            target_size = (256,256), 
#                                                            class_mode = 'categorical', 
#                                                            subset = "validation")



# # Generate a batch of 40 images and labels
# train_images, train_labels = next(train_generator)



# # Create a grid of 16 images along with their corresponding labels
# L = 4
# W = 4

# fig, axes = plt.subplots(L, W, figsize = (12, 12))
# axes = axes.ravel()

# for i in np.arange(0, L*W):
#     axes[i].imshow(train_images[i])
#     axes[i].set_title(label_names[np.argmax(train_labels[i])])
#     axes[i].axis('off')

# plt.subplots_adjust(wspace = 0.5)

# basemodel = ResNet50(weights = 'imagenet', include_top = False, input_tensor = Input(shape = (256, 256, 3)))
# basemodel.summary()

# #freezing the model upto the last stage - 4 and re-training stage -5 

# for layer in basemodel.layers[:-10]:
#   layers.trainable = False



# headmodel = basemodel.output
# headmodel = AveragePooling2D(pool_size = (4,4))(headmodel)
# headmodel = Flatten(name = 'flatten')(headmodel)
# headmodel = Dense(256, activation = 'relu')(headmodel)
# headmodel = Dropout(0.3)(headmodel)
# headmodel = Dense(128, activation = 'relu')(headmodel)
# headmodel = Dropout(0.2)(headmodel)
# headmodel = Dense(4, activation = 'softmax')(headmodel)

# model = Model(inputs = basemodel.input, outputs = headmodel)

# model.summary()

# model.compile(loss = 'categorical_crossentropy', optimizer = optimizers.legacy.RMSprop(learning_rate = 1e-4, decay = 1e-6), metrics= ["accuracy"])

# # using early stopping to exit training if validation loss is not decreasing even after certain epochs (patience)
# earlystopping = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=15)

# # save the best model with lower validation loss
# checkpointer = ModelCheckpoint(filepath="weights.hdf5", verbose=1, save_best_only=True)

# train_generator = image_generator.flow_from_directory(batch_size = 4, directory= XRay_Directory, shuffle= True, target_size=(256,256), class_mode= 'categorical', subset="training")
# val_generator = image_generator.flow_from_directory(batch_size = 4, directory= XRay_Directory, shuffle= True, target_size=(256,256), class_mode= 'categorical', subset="validation")

# with tf.device("/device:GPU:0"):
#     history = model.fit(train_generator, steps_per_epoch= train_generator.n // 4, epochs = 50, validation_data= val_generator, validation_steps= val_generator.n // 4, callbacks=[checkpointer, earlystopping])



# # serialize model to JSON
# model_json = model.to_json()
# with open("model/model.json", "w") as json_file:
#     json_file.write(model_json)
# # serialize weights to HDF5
# model.save_weights("model/model.h5")
# print("Saved model to disk")
