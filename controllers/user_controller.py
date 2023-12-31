from flask import Blueprint, jsonify, request
from models.user import User
from utils.setup import connect_db

user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.json

    # Verifique se todas as informações necessárias estão presentes
    if (
        "nome" not in data
        or "email" not in data
        or "senha" not in data
    ):
        return jsonify({"error": "Informações de cadastro incompletas"}), 400

    novo_usuario = User(
        nome=data["nome"], email=data["email"], senha=data["senha"]
    )

    email = data["email"]

    conn = connect_db()
    cursor = conn.cursor()

    # Verifique se o e-mail já está em uso
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    result = cursor.fetchall()

    if any(result):
        return jsonify({"error": "E-mail já está em uso"}), 400

    # Insira os dados do novo usuário na tabela users
    cursor.execute(
        """
        INSERT INTO users (nome, email, senha)
        VALUES (?, ?, ?)
    """,
        (novo_usuario.nome, novo_usuario.email, novo_usuario.senha),
    )

    conn.commit()
    conn.close()

    # Retorna uma resposta indicando que o usuário foi criado com sucesso
    return jsonify({"message": "Usuário criado com sucesso"}), 201


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    senha = data.get("senha")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, nome, email FROM users WHERE email = ? AND senha = ?
    """,
        (email, senha),
    )

    result = cursor.fetchone()

    if result:
        conn.close()
        return jsonify(
            {
                "message": "Informações de login corretas",
                "user": {
                    "user_id": result[0],
                    "nome": result[1],
                    "email": result[2]
                }
            }), 200
    else:
        conn.close()
        return jsonify({"error": "Informações de login inválidas"}), 401


@user_bp.route("/get_all", methods=["GET"])
def get_all():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

    users = []
    for row in result:
        user = {
            "id": row[0],
            "nome": row[1],
            "email": row[2],
            "senha": row[3],
        }
        users.append(user)

    conn.close()

    return jsonify(users), 200
