a=eval(input("Enter your list="))
reverse=[]
for i in range(len(a)-1,-1,-1):
    reverse.append(a[i])
print("Reversed array=",reverse)
