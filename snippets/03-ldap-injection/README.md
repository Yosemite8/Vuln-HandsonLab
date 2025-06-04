# CWE-90: LDAP Injection

This snippet demonstrates an LDAP injection vulnerability by simulating a login form that embeds unsanitized user input into an LDAP filter string.

## 🛠 How to Use

Start the Flask application, then issue a POST request like below:

```bash
curl -X POST [Your Service Public IP Address]/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "secret"}'
```

You should see a simulated result like:

```
Simulated LDAP bind with filter: (&(uid=admin)(userPassword=secret))
```

## 🔍 Example Payloads

```bash
# Injection attempt to bypass authentication
curl -X POST [Your Service Public IP Address]/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin)(|(uid=*)", "password": "anything"}'

# Wildcard filter injection
curl -X POST [Your Service Public IP Address]/login \
  -H "Content-Type: application/json" \
  -d '{"username": "*", "password": "*"}'
```

## 💣 What Makes It Vulnerable

- User input is directly embedded into the LDAP filter string without escaping.
- Special characters like `*`, `(`, `)`, and `|` can be injected to manipulate the filter logic.
- This could result in bypassing authentication or leaking directory data.

## ✅ Fix Suggestion

- Escape input using a function like `ldap3.utils.conv.escape_filter_chars()`.
  - Note: ldap3 library is NOT used in this handson Lab example. The lab is to simulate maliciously intended ldap filter is created perfectly.
- Avoid constructing LDAP filters via string interpolation. Use safe filter builders if available.
