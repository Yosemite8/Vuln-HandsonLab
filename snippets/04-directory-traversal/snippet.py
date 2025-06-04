# === ADD the libraries for VULNERABILITY SCENARIO ===
import os  # 🚨 used for file path operations
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask app is running. Add your first vulnerability!"

# === VULNERABILITY INSERTION POINT ===
# === VULN: Path Traversal via unsanitized filename ===
@app.route("/read")
def read_file():
    filename = request.args.get("filename")
    if not filename:
        return "Missing 'filename' parameter", 400
    try:
        with open(filename, "r") as f:
            content = f.read()
            return f"<pre>{content}</pre>"
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
