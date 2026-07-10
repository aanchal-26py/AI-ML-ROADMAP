a=int(input("Enter the lenght of the list="))
l=[]
s=0
for i in range(a):
    x=int(input(f"Enter the {i+1} element of list="))
    l.append(x)
    s=s+x
print("final list=",l)
print("Sum of all element=",s)
print("Average=",s/a)