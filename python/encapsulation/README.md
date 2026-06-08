Lesson: Encapsulation 

You already saw this:

acc.balance = -5000

Python allows it 😐
But in real systems, this is dangerous.

So we need a way to:

“Allow access, but CONTROL it”

That is Encapsulation.

🏦 Bank Example (Real Thinking)

A bank account should:

Allowed:
deposit money
withdraw money
check balance
NOT allowed:
directly set balance to anything
❌ Bad Design (No protection)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

Problem:

acc.balance = -999999

Allowed 😬

🟡 First Fix: “Protected” Convention
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

Now we say:

"_balance is internal. Don't touch directly."

But still:

acc._balance = -99999

Python still allows it.

So this is only a warning system, not real protection.

🔥 Real Encapsulation (Proper Way)

We control access using methods: