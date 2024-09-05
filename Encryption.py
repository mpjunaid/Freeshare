from cryptography.fernet import Fernet
import random, string, base64
import os

# random_string = base64.urlsafe_b64encode(os.urandom(32))


def encrypt_data(data, key):
    """Encrypts data using Fernet with the provided key."""
    print("Data encrypted")
    fernet = Fernet(key)
    return fernet.encrypt(data.encode()).decode()


def decrypt_data(data, key):
    """Decrypts data using Fernet with the provided key."""
    print("Data decrypted")
    fernet = Fernet(key)
    return fernet.decrypt(data.encode()).decode()


# print(random_string)
# print(len(random_string))
# key = Fernet.generate_key()
# print(key)
# print(len(key))
# message = encrypt_data("Hello", random_string)
# print("Encrypted message: " + message)
# print(decrypt_data(message, random_string))
