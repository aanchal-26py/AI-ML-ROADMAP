a=input("enter your string=")
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d:
    print(f'{i}:{d[i]}')