class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
        else:
            print("Insufficient funds.")

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(f"Transferred ${amount} to User {recipient.user_id}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Current Balance: ${self.balance}")

    def display_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

class ATM:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.user_id] = user

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return self.users[user_id]
        else:
            return None

def main():
    atm = ATM()

    # Create user accounts (You can create more than one user here)
    user1 = User("1234", "4321")
    atm.add_user(user1)

    while True:
        print("\nATM Menu:")
        print("1. Log In")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter your User ID: ")
            pin = input("Enter your PIN: ")

            user = atm.authenticate_user(user_id, pin)
            if user:
                print(f"Welcome, User {user.user_id}!")
                while True:
                    print("\nOperations:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer")
                    print("4. Transactions History")
                    print("5. Quit")

                    operation = input("Enter your choice: ")

                    if operation == "1":
                        amount = float(input("Enter the deposit amount: $"))
                        user.deposit(amount)
                    elif operation == "2":
                        amount = float(input("Enter the withdrawal amount: $"))
                        user.withdraw(amount)
                    elif operation == "3":
                        recipient_id = input("Enter recipient's User ID: ")
                        recipient = atm.users.get(recipient_id)
                        if recipient:
                            amount = float(input("Enter the transfer amount: $"))
                            user.transfer(recipient, amount)
                        else:
                            print("Recipient not found.")
                    elif operation == "4":
                        user.display_transactions()
                    elif operation == "5":
                        break
                    else:
                        print("Invalid operation.")
            else:
                print("Authentication failed. Please try again.")
        elif choice == "2":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
