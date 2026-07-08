'''ATM Menu (Console Application)

Display:

===== ATM =====
1. Check Balance
2. Deposit
3. Withdraw
4. Exit'''
print('''===== ATM =====
1. Check Balance
2. Deposit
3. Withdraw
4. Exit''')
choice=int(input("Enter your choice: "))
balance=50000
if choice==1:
    print(f"Your balance is: {balance}")
elif choice==2:
    deposit=int(input("Enter the amount to deposit: "))
    balance+=deposit
    print(f"Your updated balance is: {balance}")
elif choice==3:
    withdraw=int(input("Enter the amount to withdraw: "))
    balance-=withdraw
    print(f"Your updated balance is: {balance}")
elif choice==4:
    print("Thank you for using our ATM")
else:
    print("Invalid choice")