import secrets
import string

secret = []
alphabet = string.ascii_letters + string.digits + string.punctuation
for x in range(32):
	secret.append(secrets.choice(alphabet))

print("".join(secret))
