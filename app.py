# === ADD the libraries for VULNERABILITY SCENARIO ===

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask app is running. Add your first vulnerability!"

# === VULNERABILITY INSERTION POINT ===

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
