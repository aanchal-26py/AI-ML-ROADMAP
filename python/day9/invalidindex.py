a=eval(input("Enter your list="))
i=int(input("Enter index="))
try:
    print("Value=",a[i])
except IndexError:
    print("Enter correct index")
