input_file = "names.txt"
output_file = "usernames.txt"

usernames = []

with open(input_file, "r") as file:
    for line in file:
        # Ta bort radbrytningar/whitespace och gör små bokstäver
        line = line.strip().lower()

        # Replacea åäö
        line = line.replace("å", "a")
        line = line.replace("ä", "a")
        line = line.replace("ö", "o")

        # Dela upp namnen
        parts = line.split()

        first = parts[0]
        last = parts[-1]
        # last = "".join[parts[1:]]

        username1 = first + "." + last

        username2 = first[0] + last

        username3 = last + "." + first

        usernames.append(username1)
        usernames.append(username2)

        

with open(output_file, "w") as outfile:
    for user in usernames:
        outfile.write(user + "\n")

print(f"[+] Finished generating {len(usernames)} usernames")