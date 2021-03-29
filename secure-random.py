import secrets
import string

secret = []
alphabet = string.ascii_lowercase + string.ascii_uppercase + ""
for x in range(20):
	secret.append(secrets.choice(alphabet))

print("".join(secret))
