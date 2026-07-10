a=eval(input("Enter your list="))
dup=[]
for i in range(len(a)-1,-1,-1):
    dup.append(a[i])
print("Reversed list=",dup)