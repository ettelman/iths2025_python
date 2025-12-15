from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open("public_key.pem", "rb") as pub_file:
    public_key = RSA.import_key(pub_file.read())

rsa_cipher = PKCS1_OAEP.new(public_key)

message = "Secret message"
cipher_text = rsa_cipher.encrypt(message.encode())

print(cipher_text)

with open("rsa_enc_message.enc", "wb") as file:
    file.write(cipher_text)