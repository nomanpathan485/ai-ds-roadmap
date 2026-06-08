class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    

acc = BankAccount(1000)
print(acc.balance)

