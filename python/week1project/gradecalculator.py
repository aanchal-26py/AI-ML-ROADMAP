m=int(input("Enter your total marks="))
a=m/6
if a>=90:
    print("Grade A")    
elif a>80 and a<90:
    print("Grade B")
elif a>70 and a<=80:
    print("Grade C")
elif a>60 and a<=70:
    print("Grade D")
else:
    print("Fail")