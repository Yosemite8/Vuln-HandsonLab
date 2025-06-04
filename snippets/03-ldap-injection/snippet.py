# === ADD the libraries for VULNERABILITY SCENARIO ===
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask app is running. Add your first vulnerability!"

# === VULNERABILITY INSERTION POINT ===
# === VULN: LDAP Injection via POST body (username and password) ===
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    # 🚨 Vulnerable: unsanitized user input embedded into LDAP filter
    ldap_filter = f"(&(uid={username})(userPassword={password}))"
    
    # Simulated LDAP bind result
    return f"Simulated LDAP bind with filter: {ldap_filter}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
