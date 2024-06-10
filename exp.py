from werkzeug.security import generate_password_hash, check_password_hash
password = "1234"

hashed_password = generate_password_hash(password,method='pbkdf2:sha256')

print(hashed_password)

user_password = "1234"

x = check_password_hash(hashed_password,user_password)

print(x)