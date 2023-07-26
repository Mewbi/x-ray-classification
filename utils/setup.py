import sqlite3
import config

def connect_db():
    conn = sqlite3.connect(config.DATABASE)  # Nome do arquivo do banco de dados
    return conn

def read_schema_from_file():
    with open(config.SCHEMA, 'r') as file:
        return file.read()

def setup():
    schema_sql = read_schema_from_file()

    conn = connect_db()
    cursor = conn.cursor()

    sql_commands = schema_sql.split(';')
    for command in sql_commands:
        if command.strip():
            cursor.execute(command)

    conn.commit()
    conn.close()

