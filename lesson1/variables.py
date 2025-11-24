# ip_address = "10.3.10.11"
# port = 80
# is_open = True
# response_time = 0.38

# age = "38"
# print (age)

# requests_sent = 100
# responses_received = 95
# total = requests_sent // responses_received
# print (total)

# attempts = 11
# print(attempts % 2)

# base_delay = 2
# retry = 3
# delay = base_delay ** retry
# print(delay)

# result = 3+2 * 5

# attempts = 3
# attempts += 1

# attempts -= 1

# stored_password = "12345!"
# input_password = "12345!s"

# result = input_password == stored_password
# print(result)

ip = "10.3.10.11"
blocked_ip = "10.3.10.255"

print(ip != blocked_ip)

ping = 1
max_allowed = 1
print(ping >= max_allowed)

user_exists = True
is_admin = False

print(user_exists and is_admin)
print(user_exists or is_admin)
print(not is_admin)

# import keyword
# print(keyword.kwlist)

username = "bobbo"
password = 'hejsan'

hostname = "server01"
print(hostname[0])
print(hostname[-1])

# string[start:stop:step]
log_entry = "2025-11-03 LOGIN SUCCESS user=admin"
print(log_entry[:10])
print(log_entry[11:24])
print(log_entry[25:])
print(log_entry[::-1])


username = "admin"
password = "hejsan"
print(username + " " + password)

warning = "ALERT! "
print(warning * 5)

command = "GET /index HTTP/1.1"
print(len(command))

print("GET" in command)
print("apache" in command)