text = "Hello"
print (text[0])
# text[0] = 'h'
new_text = 'h' + text[1:]
print(new_text)

word = "Python"
new_word = word[:2] + 'T' + word[3:]
print(new_word)

part1 = "Login"
part2 = "success"
message = part1 + '-' + part2
print(message)

headers = ["Host: 10.3.10.11", "User-Agent: Chromium", "Accept: Json"]
packet = ", ".join(headers)
print(packet)

program = "Nmap"
print(program.upper())
print(program.lower())

msg = "login from 10.3.10.11"
print(msg.capitalize())
print(msg.title())

username = " bobbo "
print(username.strip())
print(username.lstrip())
print(username.rstrip())

log = "user=admin,ip=83.22.55.1,status=FAILED"
parts = log.split(',')
print(parts)

log = "User admin logged in from 10.3.10.11"
print(log.replace("10.3.10.11", "REDACTED"))

log = "Scan completed successfully"
print(log.find("completed"))
print(log.find("error"))

filename = "report.php"
print(filename.endswith(".txt"))
print(filename.startswith("rep"))

user = "bobbo"
ip = "10.3.10.11"
print(f"Connection established {user}@{ip}")

query = f"SELECT * FROM students WHERE name = '{user}'"
print(query)

tool = "Hydra"
targets = 10
print("Tool %s | Target: %d" % (tool, targets))
print(f"Tool {tool} | Target: {targets}")
print("Tool {tool} | Target: {targets}".format(tool=tool, targets=targets))

report = """=== SCAN SUMMARY ===
** HOST: 10.3.10.11 **
** Open ports: 22, 80, 443 **
"""
print(report)

path = "/home/bobbo/documents/code/index.php"
windows_path = "C:\\Users\\bobbo\\documents\\code\\index.php"

test = "hej hejdå"
print(test)
print(test)


shellcode = rb"\x90\x90"
raw = r"C:\Users\bobbo\documents\code\index.php"
print(raw)