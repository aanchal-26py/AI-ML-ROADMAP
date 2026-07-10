a=int(input("Enter the length of list="))
l=[]
for i in range(a):
    x=int(input(f"Enter the {i+1} element of list="))
    l.append(x)
for j in range(a):
    for i in range(len(l)-1):
            if l[i]>l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]             
print(l)