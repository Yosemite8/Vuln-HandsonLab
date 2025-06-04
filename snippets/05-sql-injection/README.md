# CWE-89: SQL Injection vulnerability

This snippet demonstrates a **SQL Injection vulnerability (CWE-89)** using unsanitized user input embedded in a raw SQL query.

## 🧠 Vulnerability Description

The application uses SQLite and directly constructs a SQL query using user-supplied input (`first_name`) without sanitization. This allows attackers to inject arbitrary SQL into the query.

```python
query = f"SELECT * FROM users WHERE first_name = '{name}'"
```

## 🚀 How to Use

1. Launch the containerized app as usual.
2. Access the root page to verify the service is running:

   ```
   http://[Your Service Public IP Address]/
   ```

3. Use the `/user` endpoint to trigger the vulnerability:

   - ✅ Normal query:
     ```
     http://[Your Service Public IP Address]/user?name=Alice
     ```

   - 🚨 SQL Injection example:
     ```
     http://[Your Service Public IP Address]/user?name=' OR '1'='1
     ```

     > ⚠️ **Note:** The above URL must be **URL-encoded** to work in browsers or scripts. For example:
     >
     > ```
     > http://[Your Service Public IP Address]/user?name=%27%20OR%20%271%27%3D%271
     > ```

   This should return all user records in the database.

## 🗂 Data Initialization

- User data is loaded at runtime from `users.json` located in the same directory.
- The SQLite database is initialized in memory (`:memory:`) with a single `users` table.

## 🔐 How to Fix (Not applied in this snippet)

To prevent SQL injection, always use parameterized queries:

```python
cursor.execute("SELECT * FROM users WHERE first_name = ?", (name,))
```

## 📁 Files

- `snippet.py` – The vulnerable Flask application
- `users.json` – External file containing dummy user records
- _(optional)_ `requirements.txt` – Lists Python dependencies

## 🏷 CWE Reference

- **CWE-89: Improper Neutralization of Special Elements used in an SQL Command (‘SQL Injection’)**
  - https://cwe.mitre.org/data/definitions/89.html
