print(''' menu:
      1.add
      2.subtract
      3.multiply
      4.divide
      5.modulus
      6.remainder''')
choice=int(input("enter your choice="))
a=int(input("enter 1st no.="))
b=int(input("enter 2nd no.="))  
if choice==1:
    c=a+b
elif choice==2:
    c=a-b
elif choice==3:
    c=a*b
elif choice==4:
    c=a/b
elif choice==5:
    c=a%b
elif choice==6:
    c=a//b
else:
    print("invalid choice")
print("result=",c)
