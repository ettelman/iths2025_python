# text = "hello"
# print(text.upper())

class Server:
    company = "Bobbocorp"

    def __init__(self, ip, os):
        self.ip = ip
        self.os = os
    
    def info(self):
        print(f"Server {self.ip} running {self.os}")

    def show_company(cls):
        print(f"Our company is {cls.company}")

    @staticmethod
    def check_vulns(service):
        print(f"Checking for vulns on {service}")

server1 = Server("10.3.10.11", "Windows 10")
server1.info()

server2 = Server("10.3.10.22", "Windows 11")
server2.info()

print(server1.company)
print(server2.company)

server2.show_company()

server2.check_vulns("FTP")



class Account:
    def __init__(self, username, active=True):
        self.username = username
        self.active = active

    def role(self):
        return "User"

class AdminAccount(Account):
    def __init__(self, username, privs):
        super().__init__(username)
        self.privs = privs

    def role(self):
        return "Administrator"

user = Account("guest")
admin = AdminAccount("root", ["read", "write", "delete"])

print(user.role())
print(admin.role())
print(admin.privs)


class Scanner:
    def __init__(self, target):
        self.target = target

    def run(self):
        raise NotImplementedError("Subclass has to implement run()")

class PortScanner(Scanner):
    def run(self):
        return f"{self.target} scanning open ports"

class VulnScanner(Scanner):
    def run(self):
        return f"{self.target} scanning for vulnerabilities"

class WebScanner(Scanner):
    def run(self):
        return f"{self.target} scanning for webvulns"

scanners = [
    PortScanner("10.3.10.11"),
    VulnScanner("10.3.10.11"),
    WebScanner("10.3.10.11")
]

for scanner in scanners:
    print(scanner.run())

class Vuln:
    def __init__(self, name, risk):
        self.name = name
        self.risk = risk

    def __str__(self):
        return f"{self.name} - Risk: {self.risk}"

vuln = Vuln("CVE-2025-55182", "Critical")
print(vuln)

class Report:
    def __init__(self, findings):
        self.findings = findings

    def __add__(self, other):
        return Report(self.findings + other.findings)

    def __str__(self):
        return f"Total findings {len(self.findings)}"

r1 = Report(["Weak Passwords", "Anonymous FTP"])
r2 = Report(["Default credentials", "HTTP"])
r3 = r1 + r2
print(r1)
print(r3)