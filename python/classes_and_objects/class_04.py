class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposite(self,amount):
        self.balance += amount
        return f"deposite: {amount}"
    def withdraw(self,amount):
        if amount > self.balance:
           return "insufficient balance"
        else:
            self.balance -= amount
            return f"withdraw: {amount}"
        
    def show_balance(self):
        return(f"{self.owner},{self.balance}")
    
acc1 = BankAccount('noaman', 1000)
print(acc1.deposite(500))
print(acc1.withdraw(200))
print(acc1.show_balance())

    
