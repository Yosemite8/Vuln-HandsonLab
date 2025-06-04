# === ADD the libraries for VULNERABILITY SCENARIO ===
import hashlib  # 🚨 MD5 is insecure
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask app is running. Add your first vulnerability!"

# === VULNERABILITY INSERTION POINT ===
# === VULN: Use of MD5 for hashing user input ===
@app.route("/hash")
def hash_input():
    user_input = request.args.get("input", "")
    hashed = hashlib.md5(user_input.encode()).hexdigest()
    return f"MD5 hash of '{user_input}' is: {hashed}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
