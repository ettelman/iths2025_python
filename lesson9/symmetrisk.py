from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(f"Generated key: {key.decode()}")

with open("secret.key", "wb") as key_file:
    key_file.write(key)


with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)
message = "Secret message".encode()
cipher_text = cipher_suite.encrypt(message)
print(cipher_text.decode())

with open("encrypted_message.enc", "wb") as enc_file:
    enc_file.write(cipher_text)

with open("encrypted_message.enc", "rb") as enc_file:
    encrypted_message = enc_file.read()

plain_text = cipher_suite.decrypt(encrypted_message)
print(f"Decrypted message: {plain_text.decode()}")