 else:
           print("Invalid withdrawl amount or insufficient balance.")
  def display_balance(self):
    print("Account balance for {} (Account #{}".format(self.__account_holder_name, self.__account_number, self.__account_balance))

account=BankAccount(account_number="222206371",account_holder_name="gowtham",initial_balance=50000.0)

account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()