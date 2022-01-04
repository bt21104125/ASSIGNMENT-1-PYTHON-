
#WRITE A PYTHON PROGRAM TO STORE VALUES IN LISTS
STUDENT=[]
SID=int(input("Enter the SID of the student= "))
Name=str(input("Enter the NAME of the student= "))
Gender=str(input("Enter the GENDER M(MALE),F(FEMALE),U(UNKNOWN) use capital letters = "))
Course_Name=str(input("Enter the COURSE NAME of the student= "))
CGPA=float(input("Enter the CGPA of the student= "))
STUDENT.append(SID)
STUDENT.append(Name)
STUDENT.append(Gender)
STUDENT.append(Course_Name)
STUDENT.append(CGPA)
print(STUDENT)
