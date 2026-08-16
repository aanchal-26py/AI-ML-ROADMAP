a=input("Enter your string:")
for i in range(0,len(a)):
    if a[i] not in a[i+1:] and a[i] not in a[:i]:
        print("First non repeating value=",a[i])
        break