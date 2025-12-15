from Crypto.PublicKey import RSA

key = RSA.generate(2048)

private_key = key.export_key()
with open("private_key.pem", "wb") as priv_file:
    priv_file.write(private_key)

public_key = key.public_key().export_key()
with open("public_key.pem", "wb") as pub_file:
    pub_file.write(public_key)