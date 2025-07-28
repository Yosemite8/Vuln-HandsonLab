# This is a skelton app.py. You can paste the contents of snippet.py to introduce vulnerability. ===

from flask import Flask

app = Flask(__name__)

# === Varidation URL: Hit ”curl -I [Your Public IP]/” to see if the app properly started ===
@app.route("/")
def index():
    return "Flask app is running. Add your first vulnerability!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
