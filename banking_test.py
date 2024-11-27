import unittest
import banking
from banking import BankAccount, BankSystem, DepositError, WithdrawalError, InsufficientFundsError

# Import necessary classes from the banking system
# Assuming the classes BankAccount, BankSystem, DepositError, WithdrawalError, InsufficientFundsError are in 'banking_system.py'
# from banking_system import BankAccount, BankSystem, DepositError, WithdrawalError, InsufficientFundsError

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        """
        Setup test cases with initial conditions.
        """
        self.account = BankAccount("John Doe", 1000.0)

    def test_deposit_valid(self):
        """Test that a valid deposit increases the balance."""
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_deposit_invalid(self):
        """Test that an invalid deposit raises DepositError."""
        with self.assertRaises(DepositError):
            self.account.deposit(-200)

    def test_withdraw_valid(self):
        """Test that a valid withdrawal decreases the balance."""
        self.account.withdraw(300)
        self.assertEqual(self.account.balance, 700)

    def test_withdraw_invalid(self):
        """Test that an invalid withdrawal (negative) raises WithdrawalError."""
        with self.assertRaises(WithdrawalError):
            self.account.withdraw(-100)

    def test_insufficient_funds(self):
        """Test that withdrawal greater than balance raises InsufficientFundsError."""
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(2000)

    def test_check_balance(self):
        """Test that the balance check returns the correct balance."""
        self.assertEqual(self.account.balance, 1000)

    def test_transaction_history(self):
        """Test that transactions are recorded correctly."""
        self.account.deposit(200)
        self.account.withdraw(100)
        self.assertEqual(len(self.account.transaction_history), 2)
        self.assertIn("Deposited 200", self.account.transaction_history)
        self.assertIn("Withdrew 100", self.account.transaction_history)


class TestBankSystem(unittest.TestCase):

    def setUp(self):
        """
        Setup test cases with initial conditions for BankSystem.
        """
        self.bank_system = BankSystem()

    def test_create_account_valid(self):
        """Test that a valid account creation works."""
        self.bank_system.create_account()  # Assuming input() is mocked or manually simulated
        self.assertTrue("John Doe" in self.bank_system.accounts)

    def test_create_account_invalid(self):
        """Test that account creation fails if account already exists."""
        self.bank_system.create_account()  # First time creation
        with self.assertRaises(DepositError):  # This will raise an error if another account is created with the same name
            self.bank_system.create_account()

    def test_login_valid(self):
        """Test that a valid login works."""
        self.bank_system.create_account()  # Creating account first
        account = self.bank_system.login()  # Mocking successful login
        self.assertIsNotNone(account)
        self.assertEqual(account.account_holder, "John Doe")

    def test_login_invalid(self):
        """Test that an invalid login fails."""
        account = self.bank_system.login()  # Login attempt before account creation
        self.assertIsNone(account)

    def test_invalid_menu_choice(self):
        """Test handling of invalid menu choices."""
        with self.assertRaises(ValueError):
            self.bank_system.run()  # Assuming the input() is handled correctly with mocks to simulate bad choices

    def test_account_menu_logout(self):
        """Test that logout works correctly."""
        self.bank_system.create_account()  # Creating account first
        account = self.bank_system.login()
        self.bank_system.account_menu(account)
        # Simulate logging out by selecting '5' from the menu
        # We cannot directly test input() here, so we would mock input or test indirectly

    def test_deposit_invalid_in_menu(self):
        """Test that invalid deposits from the account menu raise DepositError."""
        self.bank_system.create_account()
        account = self.bank_system.login()
        with self.assertRaises(DepositError):
            self.bank_system.account_menu(account)  # Simulate invalid deposit by mocking input

    def test_withdraw_invalid_in_menu(self):
        """Test that invalid withdrawals from the account menu raise WithdrawalError."""
        self.bank_system.create_account()
        account = self.bank_system.login()
        with self.assertRaises(WithdrawalError):
            self.bank_system.account_menu(account)  # Simulate invalid withdrawal by mocking input


if __name__ == "__main__":
    unittest.main()
