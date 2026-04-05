pas = input("Enter your password: ")


if len(pas) < 6:
    print("Weak password. Try using numbers and special characters.")
elif pas.isalnum:
    print("Moderate password. Try using special characters")


