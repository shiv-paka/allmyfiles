a=int(input("Enter the number of stars: "))
'''
for i in range(a): # row
    print(end=" * ")
for i in range(a):
   print(" * ")
   for j in range(a): # columns
       print(end=" A ")
   
    #for i in range(a):
#    print(a*" * ")
for i in range(a):
    print(end=" * ")
print()
print(4*"======")

c=(a-1)
for i in range(a):
    print(end=" * ")
    print(c*" "," * ")
for j in range(a):
    print(end=" * ")

print()
print(4*"======")
#prototype success? 
#works only for 4 stars T_T
d=a+1
for i in range(a):
    print(end=" * ")
print()    
for i in range(a):
    print(end=" * ")
    print(d*" "," * ")
for j in range(a):
    print(end=" * ")
print()
print(4*"======")
#sample code
d=a+1
for i in range(a):
    print(end=" * ")
print()    
for i in range(a):
    print(" A ")
    print(d*" "," * ")
for j in range(a):
    print(end=" * ")'''
'''
for i in range(a):
    print(" * ")'''
#kinda worked
for i in range(a):
     print(end=" * ")
for j in range(a):
   
    print()
    print(" * ",end=a*"  " + " * ")
print()
for i in range(a):
    print(end=" * ")

e=a-2
print()

print(" * ",end=a*" * " + " * ")
for j in range(a):
   

    print(e*" * ",end=a*"  " + e*" * ")
print()

print(" * ",end=a*" * " + " * ")

for i in range(a):
    print(end=a*" * ")
    print()
for i in range(a):
    for j in range(i):
        print(" * ",end=" ")
        print()