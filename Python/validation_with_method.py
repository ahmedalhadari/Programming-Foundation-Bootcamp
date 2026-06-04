class Account:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError ("Balance cannot be negative")
        self._balance = balance
    
    def deposit (self, amount):
        if amount <= 0:
            raise ValueError ("Deposit must be positive")
        self._balance += amount
    
    def withdraw (self, amount):
        if amount <= 0:
            raise ValueError ("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError ("Insufficient funds")
        self._balance -= amount
    def get_balance(self):
        return self._balance  
        
                     
acc1 = Account(10)
acc1.withdraw(5)
acc1.deposit(10)
acc1.deposit(10)

print (acc1.get_balance())
#acc1.deposit (5)























# x = -12
# if x < 0:
#     raise ValueError ("ERROR Message")

