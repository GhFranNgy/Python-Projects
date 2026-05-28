class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}, Balance: {self.balance}")
            return self.balance
        else:
            print("Amount must be positive")
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}, Balance: {self.balance}")
            return self.balance
        else:
            print("Invalid amount or insufficient balance")
            return False

    def get_Balance(self):
        return self.balance

    def get_Transactions(self):
        for transaction in self.transactions:
            print(transaction)


def handle_selection(selection):
    if selection == 1:
        print("-----DEPOSIT-----")
        amount_deposit = float(input("Enter amount to deposit: "))
        result = account.deposit(amount_deposit)
        if result:
            print(f"Success! New balance: {result}")
        else:
            print("Deposit failed")


    elif selection == 2:
        print("-----WITHDRAW-----")
        amount_withdraw = float(input("Enter amount to withdraw: "))
        result = account.withdraw(amount_withdraw)
        if result:
            print(f"Success! New balance: {result}")
        else:
            print("Withdraw failed")

    elif selection == 3:
        print("-----BALANCE-----")
        print(account.get_Balance())

    else:
        print("-----TRANSACTIONS-----")
        account.get_Transactions()


account_Name = input("Enter Name: ")
account_Password = input("Enter Password: ")

if account_Name == "Francisco" and account_Password == "030509":
    account = BankAccount("Francisco", 1000)

    while True:
        try:
            selection = int(input("-----Select action-----\n" \
            "(1) Deposit\n" \
            "(2) Withdraw\n" \
            "(3) Balance\n" \
            "(4) Transactions\n"))

            if selection in range(1,5):
                handle_selection(selection)
            else:
                print("Please enter a number in range of 1-4")

        except(ValueError):
            print("Please enter a valid number")

else:
    print("Get out of here")