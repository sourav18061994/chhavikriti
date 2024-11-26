Features and Workflow:
BankAccount class:

This class represents a bank account and contains methods for depositing, withdrawing, checking balance, and viewing transaction history.
The deposit() and withdraw() methods raise exceptions if the amount is invalid (zero or negative), or if there are insufficient funds for withdrawal.
BankSystem class:

This is the main class that handles account creation and login. It stores all user accounts in a dictionary, where the key is the account holder's name.
The run() method starts the banking system and provides a menu for account creation and login.
The account_menu() method is shown after logging in, where users can perform banking operations (deposit, withdraw, etc.).
Exception handling:

The program uses exception handling for invalid deposits, withdrawals, and invalid user input, ensuring the application remains robust and user-friendly.
Main flow:

Users first create an account or log into an existing one.
Once logged in, they can deposit or withdraw money, check their balance, and view transaction history.
