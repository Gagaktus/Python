import bcrypt

password = "coolPassword123"
password_bytes = password.encode("utf-8")

salt = bcrypt.gensalt()
hashed_bytes = bcrypt.hashpw(password_bytes, salt)

hashed = hashed_bytes.decode("utf-8")
print(hashed)

is_correct = bcrypt.checkpw("coolPassword123".encode("utf-8"), hashed_bytes)
print(is_correct)