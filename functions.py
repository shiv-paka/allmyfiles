'''
def my_function1():
  print("Hello from a function")
my_function1()
def myFunction(fname=" ",mname=" ",lname=" "):
  print(fname +" "+ lname +' '+ mname)
myFunction("Emil", "London", "Man")
myFunction("Tobias","","man?")
myFunction("Linus","Operating")
def fibSeq(number):
  print(number-1)'''
'''
add(12,34)
add(32,45)
sub(32,34)
sub(12,1)
div(20,2)
div(30,3)
add(32,45)
mul(12,3)
mul(45,2)
mod(12,3)
mod(24,5) 
'''
'''num=0
def add(num1,num2):
  print(num1+num2)
def sub(num1,num2):
  print(num1-num2)
def div(num1,num2):
  print(num1/num2)
def mul(num1,num2):
  print(num1*num2)
def mod(num1,num2):
  print(num1%num2)
a=int(input("Enter first number:"))
b=int(input('Enter second number:'))
print("1.Add \n" +"2. Subtract\n"+"3.Division\n"+"4.Multiplication\n"+"5.Modulus")
fun=int(input("Enter operation from 1-5:"))
if fun==1:
 add(a,b)
elif fun==2:
  sub(a,b)
elif fun==3 and b!=0:
  div(a,b)
elif fun==4:
  mul(a,b)
elif fun==5 and b!=0:
  mod(a,b)
elif fun>5:
  print("PLease enter a number between 1 & 5")
else:
  print('Division by 0 is not possible')
def toC(farenheit):
  print((farenheit+32)*1.8)
def toF(celcius):
  print((celcius-32)/1.8)
temperature=int(input("Enter temperature:"))
print("Convert to\n Celcius \n Farenheit")
conversion=input().lower()
if conversion=="celcius":
  toF(temperature)
elif conversion=="farenheit":
  toC(temperature)
else:
  print("Invalid?")
def greeting(name):
  return f"Hello {name}!!!!"
print(greeting("Shivs"))
def fibSeq(number):

fibNum=int(input("Enter the end of sequence:\n"))

fibNum=int(input("Enter the end of the sequence:\n")) #check it out
#for i in range(fibNum):
#a1=0
#b1=1
#c=a1+b1
#a1=b1
#b1=c#print(c)

def party(myMoney,friendMoney):
    if myMoney>=100 or friendMoney>=100:
        return "Chai party"
    else:
        return "Call 3rd friend for money."
mine=int(input("Money I have: "))
friend=int(input("Money friend has: "))
print(party(friend,mine))
def addOdd(ls):
  evenSum=0
  for i in range(len(ls)):
    if ls[i]%2!=0:
      evenSum=evenSum+ls[i]
  return evenSum
lst=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(addOdd(lst))
def addOdd(ls):
  evenSum=0
  for i in range(len(ls)):
    if ls[i]%2==0:
      evenSum=evenSum+ls[i]
  return evenSum
lst=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(addOdd(lst))
def vowels(li):
  count=0
  vowel="aeiou"
  for char in li:
    if char in vowel:
      count+=1
  return count
word=input("Enter something: ")
print(vowels(word))
def ind(inde):
  indx=input('Enter the word you want to check: ').lower()
  if indx in inde:
   for i in range(len(inde)):
       if indx==inde[i]:
         print(f"yes , {inde[i]} exists in the list")
         print(i)  
  else:
    print("-1")
  return inde
lst1=["apple","banana","orange"]
print(ind(lst1))
#

def findTarget(lst2,target):
  for i in range(len(lst2)):
    if lst2[i]==target:
      return i
  return -1
lst2=[1,2,3,4,5,6,7,8,9,0]
target=11
print(findTarget(lst2,target))'''
#maximum of a list
'''
def max(numli):
  for i in range(len(numli)):
    if numli[i]>=numli[i-1]:
      return numli[i] 
numLst=[10,20,50,40,30,45]
print(numLst)'''

def greet(name, age):
  print(f"Hello {name}, age= {age}")
greet("Some",17)
greet("one",20)

def Sum(a,b,c,d,e,f):
 print(a+b+c+d+e+f)
Sum(12,20,30,40,50,60)

print()

def Sums(*nums):
  total=0
  for ele in nums:
   total=total+ele 
  return total
print(Sums(1,2,3,4,5,6,7,8,9,0))
   
print("Sum calculator")
'''
def sum(*inputNums):
  sumNumLst=[]
  e=int(input("Enter the number of numbers you want to add: "))
  for i in range(e):
   sumNum=int(input(f"Enter the {i+1} number: "))
   sumNumLst.append(sumNum)
  print(sumNumLst)
  for j in range(len(sumNumLst)):
    print(sumNumLst[j])
  return j 
print()
'''
#def sum(*inputNums):
'''sumTotal=0
numEle=int(input("Enter the number of numbers: "))
for i in range(numEle):
    valEle=int(input(f"Enter the {i+1} number: "))
    return valEle
for elem in :
      sumTotal=sumTotal+elem
 # return sumTotal
print(sumTotal)
'''
#global scope
num=50
def add():
   num=10
   num2=20
   print(num+num2)
add()

def Sum():
  e=int(input("Enter the number of digits: "))
  tot=0 
  for i in range(e):
    e1=int(input(f"Enter the {i+1} number: "))
    tot=tot+e1
  print(tot)
#Sum()
       
#Sum()
#print(Sum())

sum1=int(input("Enter the first number: "))   
sum2=int(input("Enter the second number: "))   
sqr= lambda num,num1:num**num1
print(sqr(sum1,sum2))

sumLst=[1,2,3,4,5,6,7,8,9,10]
tot=0
for ele in sumLst:
  tot+=ele
print(tot)
print("========================================================")

from functools import reduce
def add(num1,num2):
  return num1+num2
sum=reduce(add,sumLst)
print(sum)
print("========================================================")
sUm=lambda a,b:a+b
suM=reduce(sUm,sumLst)
print(suM)

print("========================================================")
SuM=reduce(lambda c,d:c+d,sumLst)
print(SuM)

#PLEASE OPEN YOUR OWN FOLDER
