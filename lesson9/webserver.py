from flask import Flask, request
import sqlite3
from werkzeug.security import generate_password_hash

app = Flask(__name__)
DB_NAME = "users.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        hashed_password = generate_password_hash(password)

        try:
            conn = sqlite3.connect(DB_NAME)
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )
            conn.commit()
            conn.close()
            return "Användare skapad!"
        except sqlite3.IntegrityError:
            return "Användarnamnet finns redan!"

    return """
    <h2>Registrera</h2>
    <form method="POST">
        <input name="username" placeholder="Användarnamn"><br>
        <input name="password" type="password" placeholder="Lösenord"><br>
        <button type="submit">Registrera</button>
    </form>
    """


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
