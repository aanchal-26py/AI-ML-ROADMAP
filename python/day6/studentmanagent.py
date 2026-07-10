'''Menu:

====== MENU ======

1. Add Student
2. Display Students
3. Search Student
4. Exit

Use:

Lists
Dictionaries
Functions'''
d={}
def detailadd(name,branch,year):
    detail=[]
    detail.insert(0,name)
    detail.insert(1,branch)
    detail.insert(2,year)
    return detail
def add_student(roll,detail):
    d[roll]=detail
    print("Details added succefully")
def display_student(roll):
    print("Details of student",roll)
    print("Roll no.=",roll)
    print("Name=",d[roll][0])
    print("branch=",d[roll][1])
    print("Year=",d[roll][2])
def search_student(roll):
    if roll in d:
        print("yes this student exist")
        print("you want to see detail:")
        print('''1.yes
        2.no''')
        c=int(input("="))
        if c==1:
            display_student(roll)
    else:
        print("This student name doe not exist")
choice=0
while choice!=4:
    print('''====== MENU ======
1. Add Student
2. Display Students
3. Search Student
4. Exit''')
    choice=int(input("Enter your choice="))
    if choice == 1:
        roll=int(input("Enter student Roll no.="))
        name=input("Enter student name=")
        branch=input("Enter student branch=")
        year=int(input("Enter student year="))
        detail=detailadd(name,branch,year)
        add_student(roll,detail)
    elif choice == 2:
        roll=int(input("Enter student Roll no.="))
        display_student(roll)
    elif choice == 3:
        roll=int(input("Enter student Roll no.="))
        search_student(roll)
    elif choice == 4:
        print("Thankyou!!")
    else:
        print("Enter correct value")