from jose import jwt

SECRET_KEY = "super-secret-key"

payload = {
    "sub": "id42-artur--",
    "name": "Artur"
}

token = jwt.encode(payload, SECRET_KEY, "HS256")

print(token)

decoded = jwt.decode(token, SECRET_KEY, "HS256")
print(decoded)