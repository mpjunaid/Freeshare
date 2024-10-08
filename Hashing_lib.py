import hashlib


def create_hash(string):
    """Creates a 30-character hash from a 12-character string using SHA-256."""
    hash_object = hashlib.sha256()
    try:
        string_bytes = string.encode()
        hash_object.update(string_bytes)

    except:
        hash_object.update(string)

    hash_hex = hash_object.hexdigest()
    return hash_hex[:20]


# # Example usage
# input_string = "12345678"
# hash_value = create_hash(input_string)
# print(hash_value)
