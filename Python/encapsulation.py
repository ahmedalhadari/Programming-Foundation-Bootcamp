class Account:
    def __init__(self, owner, balance):
        self.owner = owner           # Public  - anyone can read/change 
        self._notes = "CEO Account"  # protected - "please ddon't use it from outside"
        self.__balance = balance     # private - harder to access
    def get_balance(self):
        return self.__balance   
a1 = Account("Ahmed", 1000)

print (a1.owner)
print (a1._notes)
print (a1.__balance)     # AttributeError 
print (a1.get_balance())