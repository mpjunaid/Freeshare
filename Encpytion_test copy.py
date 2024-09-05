from cryptography.fernet import Fernet
import random, string

random_string = "".join(
    random.choice(string.ascii_lowercase) for _ in range(44)
).encode()


def encrypt_data(data, key):
    """Encrypts data using Fernet with the provided key."""
    fernet = Fernet(key)  # Remove the .encode() here
    return fernet.encrypt(data.encode()).decode()


def decrypt_data(data, key):
    """Decrypts data using Fernet with the provided key."""
    fernet = Fernet(key)  # Remove the .encode() here
    return fernet.decrypt(data.encode()).decode()


print(random_string)
print(len(random_string))
key = Fernet.generate_key()
print(key)
print(len(key))
message = encrypt_data("Hello", random_string)
print("Encrypted message: " + message)
print(decrypt_data(message, random_string))
