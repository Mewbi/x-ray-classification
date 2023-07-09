from flask import jsonify, request
from models.image import Image

def classify():

    # Check image was sended
    if 'image' not in request.files:
        return jsonify({'error': 'No image found in request'}), 400
    
    image = Image(request.files['image'])

    print(image.classify())

    return jsonify({'image': 'Boooom'}), 200
