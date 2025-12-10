# try:
#     result = 10 / 1
# except ZeroDivisionError:
#     print("Division med noll är inte ok")

# try:
#     port = int(input("Give me a port number please:"))
#     print(port)
# except ValueError:
#     print("Error. Only integers")

# FileNotFoundError
# PermissionError
# TimeoutError
# KeyboardInterrupt

# raise TimeoutError

# try:
#     port = int(input("Port:"))
#     result = 10 / port
# except (ValueError, ZeroDivisionError):
#     print("Error. Port not valid")

try:
    ip = input("IP: ")
    port = int(input("Port:"))
except ValueError:
    print("Invalid port, choose an integer")
except KeyboardInterrupt:
    print("\nOperation aborted")
else:
    print(f"Scanning port {port} on IP: {ip}")
finally:
    print("Program is done")

