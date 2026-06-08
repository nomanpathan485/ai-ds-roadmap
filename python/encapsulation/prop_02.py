class BankAccount:
    def __init__(self,balance):
        self._balance = balance
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if value <0:
            print("balance cannot be negative")
            return
        self._balance = value

acc = BankAccount(100)
acc.balance = -500