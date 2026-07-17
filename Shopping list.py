shopping = []

while True:

    print("\n===== SHOPPING LIST =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show List")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item: ")
        shopping.append(item)
        print("Item added successfully!")

    elif choice == "2":
        item = input("Enter item to remove: ")

        if item in shopping:
            shopping.remove(item)
            print("Item removed!")
        else:
            print("Item not found!")

    elif choice == "3":

        print("\nShopping List:")

        if len(shopping) == 0:
            print("List is empty.")
        else:
            for item in shopping:
                print("-", item)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
