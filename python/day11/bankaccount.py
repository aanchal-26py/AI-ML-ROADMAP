class bank:
    money=0
    def __init__(self,money):
        self.money=money
    def withdraw(self):
        amount=int(input("Enter amount to withdraw="))
        self.money=self.money-amount
    def deposit(self):
        amount=int(input("Enter amount to deposit="))
        self.money=self.money+amount
    def display(self):
        print(self.money)
n=int(input("Enter total amount="))
a=bank(n)
a.withdraw()
a.display()
a.deposit()
a.display()