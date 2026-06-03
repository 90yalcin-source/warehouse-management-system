while True:
    print("WAREHOUSE SYSTEM")
    print("1. Add Product")
    print("2+. Exit(Any number or grather than 2 will exit)")

    choice = input("Select an option: ")

    if choice == "1":
        print("Opening Add Product wizard...")
    elif choice.isdigit() and int(choice) > 2:
        print("GOODBYE!!! ...")
        break
    else:
        print("Invalid option! Please try again.")
