def main():
    while True:
        print("===Main menu===")
        print("1. Choice 1")
        print("2. Choice 2")
        print("3. Exit program")

        choice = input("Choose between 1-3: ")

        match choice:
            case "1":
                print("You selected 1")
            case "2":
                print("You selected 2")
            case "3":
                print("Exiting")
                break

main()