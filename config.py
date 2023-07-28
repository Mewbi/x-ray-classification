DATABASE = "database.db"
import sqlite3


def connect_db():
    conn = sqlite3.connect("database.db")  # Nome do arquivo do banco de dados
    return conn


def load(app):
    # Restante do código existente...

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Crie a tabela "users" se ela não existir
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    """
    )

    conn.commit()
    conn.close()


ia = {"model_json": "ia/model/model.json", "model_h5": "ia/model/model.h5"}
