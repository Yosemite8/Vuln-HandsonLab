# === Thit is SKELTON app.py you can COPY from snippet.py its entire contents and PASTE them ===

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask app is running. Add your first vulnerability!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
