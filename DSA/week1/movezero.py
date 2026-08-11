a=eval(input("Enter your list="))
start=[]
end=[]
for i in a:
    if i==0:
        end.append(i)
    else:
        start.append(i)
print(start+end)