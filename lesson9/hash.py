import hashlib

data = "Secret message"
hash_object = hashlib.sha256()
hash_object.update(data.encode())
hash_value = hash_object.hexdigest()

print(f"SHA256: {hash_value}")