a=eval(input("Enter the list="))
l=a[0]
s=a[0]
for i in a:
    if i>l:
        l=i
for j in a:
    if j !=l:
        if j>s:
            s=j
print("Second largest=",s)