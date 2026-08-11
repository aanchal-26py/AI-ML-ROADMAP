a=eval(input("Enter your list="))
element=int(input("Enter the element searching for="))
for i in a:
    if element==i:
        print("Element is at position=",a.index(i)+1)