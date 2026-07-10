l=eval(input("Enter list="))
dup=[]
for i in l:
    if i not in dup:
        dup.append(i)
print("After removal of duplication=",dup)