"""a=6
b=3
print(a|b)""" #The oputput is 7, idk how though.

#100 year calculatorrrr
"""print("Welcome to the 100 year calculator")
input("What is your name?\n")
a=int(input("How old are you\n"))
b=int(input("Enter current year\n"))
print("The year you were born in =", b-a)
c=100-a
print ("The year you turn 100 will be=",c+b) """

#prototype 1 (success)
"""print("Calculator Pro")
a=int(input("Enter the first number:\n"))
b=int(input("Enter the second number:\n"))
x=["addition","add"]
y=["subtraction","subtract"]
k=["multiplication","multiply"]
l=["divide","division"]
d=input("What operation would you like me to perform?\n").lower()
if d in x:
   print(a+b)
elif d in y:
   print(a-b)
elif d in k:
   print(a*b)
elif d in l and b!=0:
   print(a/b)
elif d in l and b==0:
   print("You cannot divide by 0")

if d not in x+y+k+l:
    print("Invalid Operation")
"""

#prototype 2
"""print("Calculator Pro")
a=int(input("Enter the first number:\n"))
b=int(input("Enter the second number:\n"))

my_dict = {
        "Add":'+',
        'Subtract':'-',
        'Multiply':'*',
        'Divide' : '/'
}
c=input("What operation would you like to perform?\n")
md=my_dict[c]
if c in my_dict:
    
 if md == "+":
        print("Result:", a + b)
elif md == "-":
        print("Result:", a - b)
elif md == "*":
        print("Result:", a * b)
elif md == "/":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", a / b)
else:
    print("Invalid Operation")"""

# prototype 1
"""print("Age in months calculator")
a=int(input("Enter your age (in years)"))
print(a*12)"""
#Age in months calculator
#prototype 2 (success hehehehehehehe)
# their age , their birth month , and the current month
# year of birth and birth month + current year + current month 
print("Age in months calculator")
x=int(input("Enter year of birth\n"))
y=int(input("Enter current year\n"))
z=y-x
if x>y:
    print("Please check the data you've entered")
    quit()
elif x<1925:
    print("Damn bro")
    quit()
else :
    print("You are",z,"years old")

a=int(input("Enter the month you were born in(in numbers from 1->12) \n"))
b=int(input("Enter the current month (in numbers from 1->12) \n"))
c=b-a
d=a-b
if a>12 and b>12 :
    print("Are you sure you're from Earth? :)")
    quit()
if b>a:
     print((z*12)+c)
elif a>b:
    print((z*12)-d)
else:
    print(z*12) 
