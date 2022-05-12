import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.metrics import SparseCategoricalAccuracy
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications import VGG16 # Pre-trained VGG16 model

CIFAR10 = tf.keras.datasets.cifar10 # Use CIFAR10 dataset
(x_train, y_train), (x_valid, y_valid) = CIFAR10.load_data()
y_train = np.squeeze(y_train) # reduce demension
y_valid = np.squeeze(y_valid)

# data conversion 
def convert_data(x, y):
    x = tf.cast(x, tf.float32) # float32
    x /= 255. # pixcel normalization 
    return x, tf.cast(y, tf.int32)

train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)) 
valid_ds = tf.data.Dataset.from_tensor_slices((x_valid, y_valid)) 
AUTOTUNE = tf.data.experimental.AUTOTUNE 
train_ds = train_ds.shuffle(len(x_train)) 
train_ds = train_ds.repeat(1) 
train_ds = train_ds.batch(50) 
train_ds = train_ds.map(lambda x, y: tf.py_function(convert_data, [x, y], Tout=[tf.float32, tf.int32])) 
train_ds = train_ds.prefetch(buffer_size=AUTOTUNE) 
valid_ds = valid_ds.batch(50)
valid_ds = valid_ds.map(lambda x, y: tf.py_function(convert_data, [x, y], Tout=[tf.float32, tf.int32]))

# Pre-Trained VGG16
vgg16 = VGG16(include_top=False, weights='imagenet', input_shape=(32, 32, 3), pooling='avg')
h = Dropout(0.3)(vgg16.output)
h = Dense(256, activation='relu', name='dense01')(h) 
output = Dense(10, activation='softmax', name='output1')(h) 
vgg16.trainable = True 
model = Model(inputs=vgg16.input, outputs=output) 
model.summary()

model.compile(optimizer=Adam(0.0001), loss='sparse_categorical_crossentropy', metrics=SparseCategoricalAccuracy())   
with tf.device('/device:GPU:0'):
    model.fit(train_ds, epochs=10, validation_data=valid_ds, use_multiprocessing=True)
