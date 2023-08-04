import base64
import io
import os
import sqlite3
from flask import jsonify, request
from models.image import Image as Img
from utils.setup import connect_db
import matplotlib.pyplot as plt
from PIL import Image

def classify():
    data = request.json
    # Check image was sended

    if 'image' not in data:
        return jsonify({'error': 'No image found in request'}), 400

    if 'user_id' not in data:
        return jsonify({"error": "Missing user_id info"}), 400

    if 'username' not in data:
        return jsonify({"error": "Missing username info"}), 400

    if 'age' not in data:
        return jsonify({"error": "Missing age info"}), 400

    if 'name' not in data:
        return jsonify({"error": "Missing name info"}), 400

    if 'date' not in data:
        return jsonify({"error": "Missing date info"}), 400

    image_b64 = data['image']
    image_bin = base64.b64decode(image_b64)
    user_id = int(data['user_id'])
    username = data['username']
    age = int(data['age'])
    name = data['name']
    date = data['date']

    image = Img(
        image_bin,
        user_id,
        username,
        age,
        name,
        date)
    

    result = image.report()
    image.result = result["classification"]

    conn = connect_db()
    cursor = conn.cursor()

    # Check image already exist
    cursor.execute("SELECT * FROM classifications WHERE hash = ? AND user_id = ?", (image.hash, image.user_id,))
    result = cursor.fetchall()

    if any(result):
        return jsonify({"error": "Image already classified"}), 400

    # Insert in database
    cursor.execute(
        """
        INSERT INTO classifications (user_id, username, age, name, date, hash, result, image)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (image.user_id, image.username, image.age, image.name, image.date, image.hash, image.result, image.image_raw),
    )

    conn.commit()
    conn.close()

    response = {
        "hash": image.hash,
        "user_id": image.user_id,
        "username": image.username,
        "age": image.age,
        "name": image.name,
        "date": image.date,
        "result": image.result
    }

    return jsonify(response), 200

def get_all_imagens():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM classifications")
    result = cursor.fetchall()

    classificacoes = []
    for row in result:
        imagem = base64.b64encode(row[8]).decode('utf-8')
        classificacao = {
            'id': row[0],
            'user_id': row[1],
            'username': row[2],
            'age': row[3],
            'name': row[4],
            'date': row[5],
            'hash': row[6],
            'result': row[7],
            'image': base64.b64encode(row[8]).decode('utf-8') if row[8] else None
        }
        classificacoes.append(classificacao)
    conn.close()

    return jsonify(classificacoes), 200

def list_classficiations_user(id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, user_id, username, age, name, date, hash, result FROM classifications WHERE user_id = ?", (id,))
    result = cursor.fetchall()

    classificacoes = []
    for row in result:
        classificacao = {
                'id': row[0],
                'user_id': row[1],
                'username': row[2],
                'age': row[3],
                'name': row[4],
                'date': row[5],
                'hash': row[6],
                'result': row[7]
            }
        classificacoes.append(classificacao)

    conn.close()

    return jsonify(classificacoes), 200

def get_image(hash):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT image FROM classifications WHERE hash = ?", (hash,))
    result = cursor.fetchone()

    conn.close()

    if result:
        img = result[0]
        return jsonify(
            {
                "image": base64.b64encode(img).decode('utf-8') if img else None
            }), 200
    else:
        return jsonify({"error": "Image not found"}), 404

def delete_classification(hash, user_id):
    conn = connect_db()
    cursor = conn.cursor()

    # Insert in database
    cursor.execute(
        """
        DELETE FROM classifications WHERE hash = ? AND user_id = ?
        """,
        (hash, user_id),
    )

    conn.commit()
    conn.close()

    response = {
        "hash": hash,
        "user_id": user_id
    }

    return jsonify(response), 200
