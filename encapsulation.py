# class Bank:
#     def __init__(self, name, balance):
#         self._name = name
#         self.__balance = balance
#
#     def deposit(self):
#         return f'{self._name} deposit {self.__balance}'
#
#     def get_balance(self):  # Method to access the balance attribute
#         return self.__balance
#
# class Account(Bank):
#     def __init__(self, name, balance, account_type):
#         super().__init__(name, balance)
#         self.account_type = account_type
#
#     def balance(self):
#         return f'{self._name} deposit {self.get_balance()} and {self.account_type}'
#
# bank = Bank('Bank', 100)
# account = Account('Bob', 5000, 'deposit')
# print(account.balance())





# class BankAccount:
#     def __init__(self, account_number, account_holder):
#         self.__account_number = account_number
#         self.__account_holder = account_holder
#         self.__balance = 0.0  # Private attribute
#
#     # Method to get the account balance
#     def get_balance(self):
#         return self.__balance
#
#     # Method to deposit money into the account
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}. New balance: {self.__balance}")
#         else:
#             print("Deposit amount must be positive.")
#
#     # Method to withdraw money from the account
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.__balance}")
#         else:
#             print("Invalid withdrawal amount or insufficient funds.")
#
#     # Method to get account details
#     def get_account_details(self):
#         return {
#             "Account Number": self.__account_number,
#             "Account Holder": self.__account_holder,
#             "Balance": self.__balance
#         }
#
#
# account = BankAccount("123456789", "John Doe")
#
# account.deposit(1000)
# account.deposit(500)
#
# account.withdraw(300)
# account.withdraw(1500)  # Should print an error message
#
# print("Current balance:", account.get_balance())
#
# print("Account details:", account.get_account_details())







class Account:
    def __init__(self, account_number, account_holder, balance):
        self._account_number = account_number
        self._account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


class SavingAccount(Account):
    def __init__(self, account_number, account_holder, balance):
        super().__init__(account_number, account_holder, balance)

    def check_bonus(self):
        if self.get_balance() > 100000:  # Check if balance is more than one lakh
            bonus_amount = 0.05 * self.get_balance()  # Calculate bonus (5% of balance)
            print(f"Bonus of {bonus_amount} added to the account.")
            # self.deposit(bonus_amount)


class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance):
        super().__init__(account_number, account_holder, balance)

    


# Example Usage
saving_account = SavingAccount("1111111", "rafiq", 120000)
current_account = CurrentAccount("2222222", "ratul", 500000)

print("Saving Account:")
saving_account.check_bonus()
print("Current Account Balance:", current_account.get_balance())
