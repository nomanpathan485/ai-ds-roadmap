class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance
#objects
acc = BankAccount("noaman",1000)
acc.deposit(500)

print(acc.get_balance())



'''Notice:
_balance

instead of
balance
The single underscore means:
"Dear programmer, please don't touch this directly."
It is not truly private.
It is a warning.

Example:
acc = BankAccount("Noman", 1000)
print(acc._balance)

Still works.
Python allows it.

But professional developers understand:
I shouldn't access _balance directly.
So How Should We Access It?
Through methods.'''

    