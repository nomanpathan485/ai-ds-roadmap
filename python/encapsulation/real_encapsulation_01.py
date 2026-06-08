class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposite(self,amount):
        self._balance += amount
    def withdraw(self,amount):
        if amount > self._balance:
            return "insufficient balance"
        self._balance -= amount

    def get_balance(self):
        return self._balance
    
acc = BankAccount("noaman", 2000)
acc.deposite(2000)
print(acc.get_balance())

