a=input("Enter your first string=")
b=input("Enter your second string=")
if len(a)==len(b):
    d1={}
    d2={}
    for i in a:
        if i not in d1:
                d1[i]=1
        else:
                d1[i]+=1
    for i in b:
          if i not in d2:
                  d2[i]=1
          else:
                  d2[i]+=1
    if d1==d2:
        print("String are Anagram")
    else:
        print("String are not Anagram")