choice=0
while choice != 5:
    print(''' menu:
      1.add
      2.subtract
      3.multiply
      4.divide
      5.exit''')
    try:
        choice=int(input("enter your choice="))
        a=int(input("enter 1st no.="))
        b=int(input("enter 2nd no.="))  
    except ValueError:
        print("Invalid Input")
    else:
        if choice==1:
            c=a+b
        elif choice==2:
            c=a-b
        elif choice==3:
            c=a*b
        elif choice==4:
            try:
                c=a/b
            except ZeroDivisionError:
                print("Zero divisible error")
        print("result=",c)
