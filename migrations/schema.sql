CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL,
    idade INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS classifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    username TEXT NOT NULL,
    age INTEGER NOT NULL,
    name TEXT NOT NULL,
    date TEXT NOT NULL,
    hash TEXT NOT NULL,
    result TEXT NOT NULL,
    image BLOB
);