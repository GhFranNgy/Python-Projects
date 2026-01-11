spaceperChar = 2
firstName = input("Enter your first name: \n")
lastName = input("Enter your last name: \n")

print(
    f"Your first name {firstName} has {len(firstName)} characters\n"
    f"Your last name {lastName} has {len(lastName)} characters \n"
    f"Your full name {firstName} {lastName} has >> {len(firstName + lastName)} << characters"
    f" and takes up {len(firstName + lastName) * spaceperChar} Bytes"
)
