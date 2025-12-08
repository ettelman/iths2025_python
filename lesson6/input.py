# user_input = input("Write something:")
# print(user_input)

# user_input = input("Write a number:")
# if user_input.isdigit():
#     user_number = int(user_input)
# else:
#     print("Choose a number")

# try:
#     user_input = input("Choose a number: ")
#     user_number = int(user_input)
#     print(f"You choose {user_number}")
# except ValueError:
#     print("Input wasn't a number")


while True:
    user_input = input("Choose a number between 1-10: ")
    try:        
        user_number = int(user_input)
        if 1 <= user_number <= 10:
            print(f"You choose {user_number}")
            break
        else:
            print("Number is not between 1 and 10")
    except ValueError:
        print("Input wasn't a number")