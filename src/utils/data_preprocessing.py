import tensorflow as tf
import numpy as np

def preprocess_ktp(image):
    # Convert the image to a numpy array
    img_array = tf.keras.preprocessing.image.img_to_array(image)

    # Expand dimensions to fit the model's input shape
    img_array = np.expand_dims(img_array, axis=0)

    # Preprocess the image
    img_array /= 255.

    return img_array