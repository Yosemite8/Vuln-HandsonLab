# CWE-22: Path Traversal

This snippet demonstrates a classic Path Traversal vulnerability, where user input is used to construct a file path without validation. An attacker can traverse directories using `../` to access unauthorized files on the server.

## 🛠 How to Use

Start the Flask application, then issue a GET request like below:

```bash
curl "[Your Service Public IP Address]/read?filename=sample.txt"
```

You should see output similar to the content of `sample.txt` (if it exists in the working directory).

## 🔍 Example Payloads

```bash
# Attempt to read system file
curl "[Your Service Public IP Address]/read?filename=../../etc/passwd"

# Attempt to read OS version
curl "[Your Service Public IP Address]/read?filename=../../etc/os-release"
```

## 💣 What Makes It Vulnerable

- The file name is taken directly from user input and used without sanitization.
- Using `../` in the path allows attackers to navigate out of the intended directory and access arbitrary files.

## ✅ Fix Suggestion

- Sanitize or normalize paths using `os.path.abspath()` and validate that the resolved path stays within an allowed base directory.
- Maintain a whitelist of accessible files or file extensions.
