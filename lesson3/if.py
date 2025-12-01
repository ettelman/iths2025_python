if True:
    pass
# elif:

# else:

password = input("Ange lösenord: ")

if len(password) < 8:
    print("För kort lösenord (minst 8 tecken)")
elif password.isnumeric():
    print("Lösenordet får inte bestå av bara siffor")
else:
    print("Bra lösenord")  