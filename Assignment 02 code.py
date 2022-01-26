#Question 1 Python Code for the input string 
print("Solution of Ques.No.1 Using Different string operations")
print(" ")
a=("Python is a case sensitive language")
#Part(a)
print(len(a))
print(" ")
#Part(b)
print(a[::-1])
print(" ")
#Part(c)
new_string=a[10:26]
print(new_string)
print(" ") 
#Part(d)
print(a.replace("a case sensitive","object oriented"))
print(" ")
#Part(e)
print(a.index("a"))
print(" ") 
#Part(f)
print(a.replace(" ",""))
print(" ")


#Question 2 Storing different values in string by using string formatting
print("Solution of Ques.No.2 Storing different variables in the string after formatting")
NAME="Keshav Singh"
SID=21104125
DEPARTMENT_NAME="Electrical Engineering"
CGPA="9.9"
print("Hey", NAME ,"Here !" )
print("My SID is",SID  )
print("I am from" ,DEPARTMENT_NAME, "department and my CGPA is", CGPA)
print(" ")


#Question 3 Using bitwise operators to calculating following  parts
print("Solution of Ques.No.3 Using bitwise operator to calculate the following")
#a=56 b=10
a=0b111000
b=0b1010
print("Part a")
#(a&b)  
print(bin(a&b))
print(" ")
print("Part b")
#(a|b)  
print(bin(a|b))
print("  ")
print("Part c")
#(a^b)
print(bin(a^b))
print(" ")
print("Part d")
#(Left side both  a and b with 4 bits ")
print(bin(a<<2))
print(bin(b<<2))
print(" ")
print("Part e")
#(Right side a with 2 bits  and b with 4 bits ")
print(bin(a>>2))
print(bin(b>>4))
print(" ")


#Question 4 Python program to find the greatest number among the three Entered number by the user
print("Solution of Ques.No.4 Finding Greatest Number among he three entered number  ")
a=int(input("Enter the First number="))
b=int(input("Enter the Second number="))
c=int(input("Enter the Third number="))
if a>b and a>c:
    print("a is the greatest number among three number")
elif b>a and b>c:
      print("b is the greatest number among three number")
else :
      print("c is the greatest number among three number")
print(" ")


#Question 5 Checking the word "name" in the string entered by the user
print("Solution of Ques.No.5 Finding word(name) in the entered string by the user")
string=str(input("Enter the string="))
if "name" in string:
        print("Yes")
else:
    print("No")
print(" ")


#Question 6 Testing the crieteria to fulfill the forming a triangle by entering three sides by the user
print("Solution of Ques.No.6 Test to form a triangle by entered ")
a=float(input("Enter the First side of triangle="))
b=float(input("Enter the Second side of triangle="))
c=float(input("Enter the Third side of triangle="))
if a>b+c:
    print("Triangle can not be formed")
elif b>a+c:
    print("Triangle can not be formed")
elif c>a+b:
    print("Triangle can not be formed")
else:
    print("Triangles is formed")
print(" ")

    









