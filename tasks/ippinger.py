import os
import platform


def ping_ip(ip):
    if platform.system().lower() == "windows":
        response = os.system(f"ping -n 1 {ip} > NUL 2>&1")
    else:
        response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    return response


with open("ip.txt", "r") as file:
    ips = file.read().splitlines()

with open("results.txt", "w") as results:
    for ip in ips:
        if ping_ip(ip):
            result = f"{ip} is available"
        else:
            result = f"{ip} is unavailable"
        print(result)
        results.write(result + "\n")

