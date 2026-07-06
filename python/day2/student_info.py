'''Student Information System
Ask the user for:
Name
Age
College
Branch
CGPA
Print the output neatly using f-strings.'''
name=input("Enter your name=")
age=int(input("Enter your age="))
college=input("Enter your college name=")
branch=input("Enter your branch=")
cgpa=float(input("Enter your CGPA="))
print(f'''Student Information:
Name    |\t{name}
Age     |\t{age}
College |\t{college}
Branch  |\t{branch}
CGPA    |\t{cgpa}''')