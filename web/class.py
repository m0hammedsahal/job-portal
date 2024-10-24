class Account:
    def __init__(self, account_number, account_balance):
        self.account_number = account_number
        self.account_balance = account_balance

    def deposite(self, deposite_amount):
        self.account_balance = self.account_balance + deposite_amount

    def withdraw(self, amount):
        if self.account_balance - amount > 0:
            self.account_balance = self.account_balance - amount
            print("withdraw successful")

        else:
            print("withdraw failed")

    def display(self):
        print("Your Account balance is {}".format(self.account_balance))


ac_one = Account('A123', 5000)
ac_two = Account('A124', 1000)

deposite_amount = int(input("Enter The Deposite Amount"))
ac_one.deposite(deposite_amount)

amount = int(input("Enter The withdawal Amount"))
ac_one.withdraw(amount)
ac_one.display()