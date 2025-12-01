# file = open("textfil.txt", "r")
# file.close

file = open("usernames.txt", "r")
content = file.read()
print(content)
file.close

file = open("usernames.txt", "r")
line = file.readline()
while line:
    print(line, end='')
    line = file.readline()
file.close()

file = open("usernames.txt", "r")
lines = file.readlines()
for line in lines:
    print(line, end='')
file.close

print("")

file = open("usernames.txt", "r")
content = file.read().splitlines()
for line in content:
    print(line)
file.close

file = open("test.txt", "w")
file.write("This is line 1\n")
file.write("This is line 2")
file.close()

file = open("test.txt", "a")
file.write("\nThis is line 3")
file.close()

with open("testa.txt", "r") as file:
    content = file.read()
    print(content)
print ("")

