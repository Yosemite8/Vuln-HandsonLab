# === ADD the libraries for VULNERABILITY SCENARIO ===
import os  # 🚨 used for command execution
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask app is running. Add your first vulnerability!"

# === VULNERABILITY INSERTION POINT ===
# === VULN: OS Command Injection via POST body ===
@app.route("/run", methods=["POST"])
def run_command():
    data = request.get_json()
    command = data.get("command") if data else None
    if not command:
        return "Missing 'command' in request body", 400
    # 🚨 Vulnerable: unsanitized input passed directly to the shell
    stream = os.popen(command)
    output = stream.read()
    return f"<pre>{output}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
