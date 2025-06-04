# === ADD the libraries for VULNERABILITY SCENARIO ===
import sqlite3  # 🚨 vulnerable SQL usage
import json
from flask import Flask, request

app = Flask(__name__)

# Load users from external JSON file
with open("users.json", "r") as f:
    users = json.load(f)

# Initialize in-memory SQLite database
conn = sqlite3.connect(":memory:", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        password_hash TEXT,
        age INTEGER,
        gender TEXT,
        ssn TEXT,
        credit_score_level TEXT,
        credit_comment TEXT
    )
""")
for user in users:
    cursor.execute("""
        INSERT INTO users (id, first_name, last_name, email, password_hash, age, gender, ssn, credit_score_level, credit_comment)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        user["id"],
        user["first_name"],
        user["last_name"],
        user["email"],
        user["password_hash"],
        user["age"],
        user["gender"],
        user["ssn"],
        user["credit_score_level"],
        user["credit_comment"]
    ))
conn.commit()

@app.route("/")
def index():
    return "Flask app is running. Add your first vulnerability!"

# === VULNERABILITY INSERTION POINT ===
# === VULN: SQL Injection via unsanitized first_name parameter ===
@app.route("/user")
def get_user():
    name = request.args.get("name", "")
    # 🚨 Vulnerable: user input directly inserted into SQL query
    query = f"SELECT * FROM users WHERE first_name = '{name}'"
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            output = ""
            for row in rows:
                output += f"<p>{row}</p>"
            return output
        else:
            return "No such user found."
    except Exception as e:
        return f"Query failed: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
