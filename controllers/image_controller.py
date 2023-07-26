from flask import jsonify, request
from models.image import Image
from utils.setup import connect_db

def classify():

    # Check image was sended
    if 'image' not in request.files:
        return jsonify({'error': 'No image found in request'}), 400

    if 'user_id' not in request.form:
        return jsonify({"error": "Missing user_id info"}), 400

    if 'username' not in request.form:
        return jsonify({"error": "Missing username info"}), 400

    if 'age' not in request.form:
        return jsonify({"error": "Missing age info"}), 400

    if 'name' not in request.form:
        return jsonify({"error": "Missing name info"}), 400

    if 'date' not in request.form:
        return jsonify({"error": "Missing date info"}), 400

    user_id = int(request.form.get('user_id'))
    username = request.form.get('username')
    age = int(request.form.get('age'))
    name = request.form.get('name')
    date = request.form.get('date')

    image = Image(
        request.files['image'],
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

    print(image.user_id, image.username, image.age, image.name, image.hash, image.result)
    # Insert in database
    cursor.execute(
        """
        INSERT INTO classifications (user_id, username, age, name, date, hash, result, image)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (image.user_id, image.username, image.age, image.name, image.date, image.hash, image.result, image.image),
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
