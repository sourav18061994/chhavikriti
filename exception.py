class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")
        print(f"Deposited {amount}. New balance is {self.balance}.")
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds!")
        self.balance -= amount
        self.transaction_history.append(f"Withdrew {amount}")
        print(f"Withdrew {amount}. New balance is {self.balance}.")
    
    def check_balance(self):
        print(f"Current balance: {self.balance}")
    
    def view_transaction_history(self):
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            print("Transaction history:")
            for transaction in self.transaction_history:
                print(transaction)

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_holder = input("Enter account holder's name: ")
        if account_holder in self.accounts:
            print("Account already exists.")
            return
        try:
            initial_balance = float(input("Enter initial deposit: "))
            if initial_balance < 0:
                raise ValueError("Initial deposit must be a positive value.")
            new_account = BankAccount(account_holder, initial_balance)
            self.accounts[account_holder] = new_account
            print(f"Account created for {account_holder}. Initial balance: {initial_balance}.")
        except ValueError as e:
            print(f"Error: {e}")

    def login(self):
        account_holder = input("Enter your name to login: ")
        if account_holder not in self.accounts:
            print("Account not found. Please create an account first.")
            return None
        return self.accounts[account_holder]

    def run(self):
        while True:
            print("\nWelcome to the Banking System!")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            try:
                choice = int(input("Enter your choice (1/2/3): "))
                if choice == 1:
                    self.create_account()
                elif choice == 2:
                    account = self.login()
                    if account:
                        self.account_menu(account)
                elif choice == 3:
                    print("Thank you for using the Banking System. Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    def account_menu(self, account):
        while True:
            print("\nAccount Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. View Transaction History")
            print("5. Logout")
            try:
                choice = int(input("Enter your choice (1/2/3/4/5): "))
                if choice == 1:
                    try:
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    except ValueError as e:
                        print(f"Error: {e}")
                elif choice == 2:
                    try:
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    except ValueError as e:
                        print(f"Error: {e}")
                elif choice == 3:
                    account.check_balance()
                elif choice == 4:
                    account.view_transaction_history()
                elif choice == 5:
                    print("Logging out...")
                    break
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    bank_system = BankSystem()
    bank_system.run()
