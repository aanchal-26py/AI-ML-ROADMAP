class bank:
    def __init__(self):
        self.money=int(input("Enter total amount="))
    def withdraw(self):
        amount=int(input("Enter amount to withdraw="))
        if self.money>=amount:
            self.money=self.money-amount
            print("money is credited")
        else:
            print("Your account has not enough money")
    def deposit(self):
        amount=int(input("Enter amount to deposit="))
        self.money=self.money+amount
    def display(self):
        print(self.money)

c=0
a=bank()
while c!=4:
    print('''1.DISPLAY
2.WITHDRAW
3.CREDITED
4.EXIT''')
    c=int(input('='))
    if c==1:
        a.display()
    elif c==2:
        a.withdraw()
    elif c==3:
        a.deposit()
    elif c==4:
        break
    else:
        print("Enter correct value")
print("Thnakyou!")