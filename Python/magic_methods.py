class Money: 
    def __init__(self, amount):
        self.amount = amount
    
    def __str__ (self):
        return f"{self.amount:.2f} SAR"
    
    def __add__ (self, other):
        return Money(self.amount + other.amount)
    
m1 = Money(500)
m2 = Money(300)
total = m1 + m2 
print (total)