"""a="Hello World!"
print(a)
print(a[5])
print(a[-4])

name=input("Enter your name\n")
print(type(name),"Hello",name + "!") 
number=int(input("Enter your age\n"))
print(type(number),number) """

"""a=int(input("Enter number a \n"))
b=int(input("Enter number b \n"))
print("Addition of ",a ,"and",b,"is",a+b)
print("Subtraction of ",a ,"and",b,"is",a-b)
print("Division of ",a ,"and",b,"is",a/b)
print("Multiplication of ",a ,"and",b,"is",a*b)
print("Modulus of ",a ,"and",b,"is",a%b)
print("Floor Division of ",a ,"and",b,"is",a//b)
print("Exponent of ",a ,"and",b,"is",a**b) """

"""a=int(input("Enter number a \n"))
b=int(input("Enter number b \n"))
add=a+b
sub=a-b
mul=a*b
div=a/b
flo=a//b
exp=a**b
mod=a%b
print("Addition of ",a ,"and",b,"is",add)
print("Subtraction of ",a ,"and",b,"is",sub)
print("Division of ",a ,"and",b,"is",div)
print("Multiplication of ",a ,"and",b,"is",mul)
print("Modulus of ",a ,"and",b,"is",mod)
print("Floor Division of ",a ,"and",b,"is",flo)
print("Exponent of ",a ,"and",b,"is",exp)"""

#Using f string to code 
"""a=int(input("Enter number a\n"))
b=int(input("Enter number b\n"))
txt=f"The price is {(a+b):.2f}"
print(txt)

#operators and if statements
print("Greater than - Less than calculator")
c=int(input("Enter number c\n"))
d=int(input("Enter number d\n"))
 
if c>d:
    print("Your answer is:")
    print("C is greater than D")
else:
    print("Your answer is:")
    print("D is greater than C") 

print(~(15))
a=[1,2,3,4,"Hello",3.14,True,4+3j]
print(a) #To print the list
print(*a) #to print the list without square brackets
print(a[3]) #Indexing (Kinda)


a[4]="Good Bye"
print(*a)
print(len(a))
a.append(7)
print(a)


b={"a",'d','c','e',True,3.14,1,2,3,3+4j}
print(b)
print(len(b))

c=(1,2,3,'HELLO',3.14,3+4j)
print(c)
print(*c)

d={
   1:1,
   2:2,
   3:'Hello World'

}
#dict={key1:value1'key2:value2,key3:value3}
print(d[3])"""

"""m=int(input("How many rows do you want?\n"))
n=int(input("How many columns do you want?\n"))
l=[[input()]*m]*n
print(l)"""

tuple=(3,(2,3,4),("Hello",'hi'),(3.14,4.32))
print(tuple)

List=[1,[3,2,3],[5,65,4],['Hello','Hi']]
print(List)

"""Set={1,2,{3,4,5},{'Hello','Hi'},{3.14,4.12}}
print(Set)""" #error

listdict=[1,2,{1:'hello',2:'Hi'}]
print(listdict)

"""setdict={1,2,{1:'hi',2:'Hellllooo'}}
print(setdict)""" #error

tupledict=(1,2,{1:'hoi',2:'Hello?'})
print(tupledict)

listset=[1,2,{1,2},{3,2}]
print(listset)

listuple=[('hello','hi')]
print(listuple)

"""setlist={1,2,[1,2,3]}
print(setlist)""" #error

setuple={1,2,(3,2,1),(4,3,2)}
print(setuple)

tuplelist=(1,2,[2,3,4])
print(tuplelist)

tupleset=(1,2,{'hello','hi'})
print(tuplelist)