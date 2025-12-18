class Account:

    def __init__(self, accountnumber):   
        self.accountnumber = accountnumber
        self.__balance = 5000            # private
        self.__pin = 1234                # private
        self._customer_id = 90909090     # protected

    def withdraw(self, userinput, pin):
        if pin == self.__pin:
            if userinput <= self.__balance:
                self.__balance -= userinput
                print(f"Withdraw Successfully: {userinput}")
            else:
                print("Insufficient Balance!")
        else:
            print("Please enter valid PIN")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit Successfully: {amount}")
        else:
            print("Invalid Amount")

    def balance(self):
        print(f"Balance: {self.__balance}")
        print(f"Account Number: {self.accountnumber}")
ob = Account(349000000)

ob.balance()
ob.deposit(2000)
ob.withdraw(1000, 1234)
ob.balance()
