from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open("private_key.pem", "rb") as key_file:
    private_key = RSA.import_key(key_file.read())

rsa_cipher = PKCS1_OAEP.new(private_key)

with open("rsa_enc_message.enc", "rb") as file:
    enc_message = file.read()

plain_text = rsa_cipher.decrypt(enc_message)
print(plain_text.decode())