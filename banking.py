import logging

# Configure the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Custom Exceptions
class DepositError(Exception):
    """Exception raised for errors in deposit amount."""
    def __init__(self, message="Deposit amount must be greater than zero."):
        self.message = message
        super().__init__(self.message)

class WithdrawalError(Exception):
    """Exception raised for errors in withdrawal amount."""
    def __init__(self, message="Withdrawal amount must be greater than zero."):
        self.message = message
        super().__init__(self.message)

class InsufficientFundsError(Exception):
    """Exception raised when there are insufficient funds for withdrawal."""
    def __init__(self, message="Insufficient funds for this withdrawal."):
        self.message = message
        super().__init__(self.message)

class BankAccount:
    """
    A class representing a bank account.

    Attributes:
        account_holder (str): Name of the account holder.
        balance (float): Current balance of the account.
        transaction_history (list): List of transactions made by the account holder.

    Methods:
        deposit(amount): Deposits a specified amount into the account.
        withdraw(amount): Withdraws a specified amount from the account.
        check_balance(): Prints the current balance of the account.
        view_transaction_history(): Prints the list of transactions made on the account.
    """
    
    def __init__(self, account_holder, initial_balance=0):
        """
        Initializes a BankAccount instance with an account holder and initial balance.

        Args:
            account_holder (str): The name of the account holder.
            initial_balance (float): The initial balance of the account (default is 0).
        """
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        logger.info(f"Account created for {account_holder} with initial balance {initial_balance}.")

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            DepositError: If the deposit amount is less than or equal to zero.
        """
        try:
            if amount <= 0:
                raise DepositError("Deposit amount must be greater than zero.")
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount}")
            logger.info(f"Deposited {amount}. New balance is {self.balance}.")
            print(f"Deposited {amount}. New balance is {self.balance}.")
        except DepositError as e:
            logger.error(f"Error: {e}")
            print(f"Error: {e}")
    
    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            WithdrawalError: If the withdrawal amount is less than or equal to zero.
            InsufficientFundsError: If there are insufficient funds.
        """
        try:
            if amount <= 0:
                raise WithdrawalError("Withdrawal amount must be greater than zero.")
            if amount > self.balance:
                raise InsufficientFundsError("Insufficient funds!")
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            logger.info(f"Withdrew {amount}. New balance is {self.balance}.")
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        except (WithdrawalError, InsufficientFundsError) as e:
            logger.error(f"Error: {e}")
            print(f"Error: {e}")
    
    def check_balance(self):
        """
        Prints the current balance of the account.
        """
        logger.info(f"Checked balance: {self.balance}")
        print(f"Current balance: {self.balance}")
    
    def view_transaction_history(self):
        """
        Prints the transaction history of the account.
        If there are no transactions, a message indicating so is displayed.
        """
        if not self.transaction_history:
            logger.info("No transactions yet.")
            print("No transactions yet.")
        else:
            logger.info("Transaction history viewed.")
            print("Transaction history:")
            for transaction in self.transaction_history:
                print(transaction)

class BankSystem:
    """
    A class representing a banking system that allows users to create accounts, deposit, withdraw, and check balances.

    Methods:
        create_account(): Allows a user to create a new bank account.
        login(): Logs the user into an existing bank account.
        run(): Runs the banking system by presenting the main menu and handling user choices.
        account_menu(account): Presents the account menu for the user to interact with their account.
    """
    
    def __init__(self):
        """
        Initializes the BankSystem with an empty dictionary of accounts.
        """
        self.accounts = {}

    def create_account(self):
        """
        Creates a new account for a user by taking the account holder's name and an initial deposit.

        Raises:
            DepositError: If the initial deposit is less than zero.
        """
        account_holder = input("Enter account holder's name: ")
        if account_holder in self.accounts:
            logger.warning(f"Attempt to create an account for {account_holder} failed. Account already exists.")
            print("Account already exists.")
            return
        try:
            initial_balance = float(input("Enter initial deposit: "))
            if initial_balance < 0:
                raise DepositError("Initial deposit must be a positive value.")
            new_account = BankAccount(account_holder, initial_balance)
            self.accounts[account_holder] = new_account
            logger.info(f"Account created for {account_holder} with initial deposit of {initial_balance}.")
            print(f"Account created for {account_holder}. Initial balance: {initial_balance}.")
        except DepositError as e:
            logger.error(f"Error: {e}")
            print(f"Error: {e}")

    def login(self):
        """
        Allows a user to log into their account by entering their name.

        Returns:
            BankAccount: The logged-in account if found, None otherwise.
        """
        account_holder = input("Enter your name to login: ")
        if account_holder not in self.accounts:
            logger.warning(f"Login attempt failed. Account for {account_holder} not found.")
            print("Account not found. Please create an account first.")
            return None
        logger.info(f"User {account_holder} logged in successfully.")
        return self.accounts[account_holder]

    def run(self):
        """
        Runs the main banking system menu, allowing the user to create an account, login, or exit the system.
        """
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
                    logger.info("User exited the banking system.")
                    print("Thank you for using the Banking System. Goodbye!")
                    break
                else:
                    logger.warning("Invalid choice entered in main menu.")
                    print("Invalid option. Please try again.")
            except ValueError:
                logger.error("Invalid input! Please enter a valid number.")
                print("Invalid input! Please enter a valid number.")

    def account_menu(self, account):
        """
        Displays the account menu, where users can deposit, withdraw, check balance, or view transaction history.

        Args:
            account (BankAccount): The logged-in user's bank account.
        """
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
                    except DepositError as e:
                        logger.error(f"Error during deposit: {e}")
                        print(f"Error: {e}")
                elif choice == 2:
                    try:
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    except (WithdrawalError, InsufficientFundsError) as e:
                        logger.error(f"Error during withdrawal: {e}")
                        print(f"Error: {e}")
                elif choice == 3:
                    account.check_balance()
                elif choice == 4:
                    account.view_transaction_history()
                elif choice == 5:
                    logger.info(f"User {account.account_holder} logged out.")
                    print("Logging out...")
                    break
                else:
                    logger.warning("Invalid choice entered in account menu.")
                    print("Invalid option. Please try again.")
            except ValueError:
                logger.error("Invalid input! Please enter a valid number.")
                print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    bank_system = BankSystem()
    bank_system.run()
