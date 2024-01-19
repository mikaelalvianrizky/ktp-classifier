import os
from datetime import datetime

from flask import Blueprint, jsonify, request
from flask_cors import CORS

import tensorflow as tf

from src.utils.data_preprocessing import preprocess_ktp

ktpApp = Blueprint('ktpApp', __name__)
CORS(ktpApp) # enable CORS on the instagramApp

ktp_classifier = tf.keras.models.load_model("src\models\ktp_classifier.h5")

@ktpApp.route('/ktp', methods=['POST'])
def validate():
    # Get image from request
    request_image = request.files['image']

    # Check if the 'image' field was sent in the request
    if request_image:
        current_dateTime = datetime.now()
        filename = f'{current_dateTime.microsecond}.{"png"}'

        # Save the file to ./tmp
        os.makedirs('/tmp', exist_ok=True)
        save_path = os.path.join('/tmp', filename)

        request_image.save(save_path)

    # Load the image you want to predict
    image = tf.keras.preprocessing.image.load_img(save_path, target_size=(180,180))

    # Prepocess the image
    image = preprocess_ktp(image)
    
    # Get the prediction
    predictions = ktp_classifier.predict(image)[0][0]
    predictions = round((1-predictions)*100, 2)
    
    # Delete the tmp image
    os.remove(save_path)

    return f"KTP: {predictions}%"