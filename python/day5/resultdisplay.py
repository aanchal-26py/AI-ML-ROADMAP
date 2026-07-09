'''Student Result System

Ask the user for:

Name
Roll Number
Marks in 5 subjects

Create functions:

calculate_total()

calculate_percentage()

calculate_grade()

display_result()

Your output should look professional.'''
def calculate_total(x1,x2,x3,x4,x5):
    total= x1+x2+x3+x4+x5
    return total
def calculate_percentage(x):
    per=x/5
    return per
def calculate_grade(a):
    if a>=90:
        print("Grade A")    
    elif a>80 and a<90:
        print("Grade B")
    elif a>70 and a<=80:
        print("Grade C")
    elif a>50 and a<=70:
        print("Grade D")
    else:
        print("Fail")
name=input("Enter your name=")
rollno=int(input("roll no= "))
x1=int(input("Enter 1st subject marks= "))
x2=int(input("Enter 2nd subject marks= "))
x3=int(input("Enter 3rd subject marks= "))
x4=int(input("Enter 4th subject marks= "))
x5=int(input("Enter 5th subject marks= "))
print("\n\t====REPORT CARD====")
print("NAME     = ",name.upper())
print("ROLL NO. = ",rollno)
print("1st subject marks\t=\t",x1 )
print("2nd subject marks\t=\t",x2 )
print("3rd subject marks\t=\t",x3 )
print("4th subject marks\t=\t",x4 )
print("5th subject marks\t=\t",x5 )
marks=calculate_total(x1,x2,x3,x4,x5)
percentage=calculate_percentage(marks)
print(f"TOTAL MARKS\t=\t{marks}")
print("Percentage\t=   ",percentage)
calculate_grade(percentage)