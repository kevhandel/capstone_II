import numpy as np
import os

from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten, Activation, Dropout
from keras.layers import Dense
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator


import matplotlib.pyplot as plt
train_dir = '../figs/train'
test_dir = '../figs/test'
num_pics = 10000
num_val_pics = 2000
layers = 32
batch_size = 16
drop_out = .1
nb_epoch = 30    # number of passes through the entire train dataset before weights "final"
nb_filters = 12 # number of convolutional filters to use
# size of pooling area for max pooling
pool_size = (2, 2) # decreases image size, and helps to avoid overfitting
# convolution kernel size
kernel_size = (3,3) # slides over image to learn features
num_pics//batch_size
steps_per_epoch = num_pics//batch_size
validation_steps = num_val_pics//batch_size
def add_training():
    train_datagen = ImageDataGenerator(rescale = 1./255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True)
    test_datagen = ImageDataGenerator(rescale = 1./255)
    training_set = train_datagen.flow_from_directory(train_dir,
                        target_size = (64, 64),
                        batch_size = batch_size,
                        class_mode = 'binary')
    test_set = test_datagen.flow_from_directory(test_dir,
                        target_size = (64, 64),
                        batch_size = batch_size,
                        class_mode = 'binary')
    return test_set, training_set

test_set, training_set = add_training()

classifier = Sequential()
classifier.add(Conv2D(layers, (3,3), input_shape=(64,64,3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=pool_size))
classifier.add(Dropout(drop_out)) # zeros out some fraction of inputs, helps prevent overfitting
classifier.add(Flatten())
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dense(units=1, activation='sigmoid'))
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
classifier.fit_generator(training_set,
                        steps_per_epoch = steps_per_epoch,
                        epochs = nb_epoch,
                        validation_data = test_set,
                        validation_steps = validation_steps)

test_image = image.load_img('../figs/tts/test13_17_p2/sawtooth/sawtooth_14764_2382_64.png', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
if int(result[0][0]) == 0:
    prediction = 'sawtooth'
else:
    prediction = 'square'
print(f'prediction: {prediction}')
