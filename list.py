'''#We use lists more than array
#List
Lst1=[10,20,30,40,11,22,33,44]
print(Lst1)

lst=["Mouli",25,True] #combo of different data types
print(lst)

print(Lst1[1])
Lst1.append(23)
print(Lst1)
#insert
Lst1.insert(2,[12,21])
print(Lst1)

#extend list
Lst1.extend([60,70,80])
print(Lst1)

#slicing
print(Lst1[0:3])
print(Lst1[4:])
print(Lst1[:4])'''
"""
_____     _____ 
  |         |
  |         |
     _____          👍👍👍👍

 """ 
'''print(f'Hellllooooooooo')

for i in range(len(Lst1)):
    print(Lst1[i])

for x in Lst1:
    print(x)

lst2=[12,32,43,546,76,67,87,'Hello','hi',True,3.14]

for y in lst2:
    print(y*10)

newList=[1,2,3,4,5,6,7,8,9,10,11]
even_List=[]
Odd_List=[]
for i in range(len(newList)):
    if newList[i]%2==0:
        even_List.append(newList[i])
    else:
        Odd_List.append(newList[i])
    
print(f'Odd list is {Odd_List} and Even List is {even_List}')'''

'''sumList=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(sumList)):
    print(sum(sumList))
    break

sumList1=[1,2,3,4,5,6,7,8,9,10,11]
sum=0
for ele in sumList1:
    sum=sum+ele
print(sum/len(sumList1))
'''
#List indexing question
'''emtyList=[]
size=int(input('Enter list size:'))
for i in range(size):
    varble=int(input('Enter the valuez:'))
    emtyList.append(varble)
print(emtyList)
check=int(input('Enter the value you want to check:'))
for i in range(size):
    if emtyList[i]==check:
        print(i)
        break
else:
    print('-1')'''
    

'''if check in emtyList:
    print(f'Yes , {check} exists in {emtyList}')
    print(emtyList[check])
    
else:
    print('No it is not in the list.')'''
#list repetition question
'''emtyList1=[]
size1=int(input('Enter list size:'))
for i in range(size1):
    varble1=int(input('Enter the valuez:'))
    emtyList1.append(varble1)
print(emtyList1)
check1=int(input('Enter the value you want to check repetition:'))
count=0
for i in range(size1):
    if emtyList1[i]==check1:
        count+=1
print(count) 
'''
#list with string 
'''strList=[]
striSize=int(input('Enter length of list:'))
#lett=input('Enter a letter to count its repetition').lower()
for i in range(striSize):
    striEle=input('Enter word:').lower()
    strList.append(striEle)
print(strList)
striJoin="".join(strList)
ch=input('Enter a letter:').lower()
striCount=0
for char in striJoin:
    if  char in ch:
        striCount+=1
print(striCount)'''

'''stng=input('Enter a string: ').lower().strip()
cha=input('Enter the character you want to find: ').lower()
cnt=0
cnt1=0
for ch in stng:
    if ch!=cha:
        cnt1+=1
    elif ch==cha:
        cnt+=1
print(f'{cha} repeats {cnt} times.')
print(f'Remaining number of characters are {cnt1}')'''

'''print("Tables(uptoX10)")
tableNum=int(input('Enter a number: '))
for i in range(1,11):
    print(f"{tableNum} X {i} = {tableNum*}")'''

'''#works
for i in range(0,5):
    print('*')
    for j in range(i+1):
        
        print('*',end=' ')
print('*',end=" ")

print()

#for i in range(0,5):
    #print('* * * * *')


for i in range(0,5):
    for j in range(0,5):
        print('*',end=" ")
    print()


#calculates them together
cnt=0
aniLst=["Dog","Kangaroo","Bird"]
for i in range(len(aniLst)):
    for ch in aniLst[i]:
        cnt+=1
    print(cnt)

#calculates them individually
aniLst=["Dog","Kangaroo","Bird"]
for i in range(len(aniLst)):
     print(len(aniLst[i]))


for i in range(0,5):
    for j in range(0,5):
        print([j,i],end=" ")
    print()'''

'''for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()'''
'''j=6
i=0

for i in range():
    for j in range():
        print("*",end=" ")
print()'''
'''d=1
for i in range(5):
    
    for j in range(4-i):
        print(end="  ")
    
    for s in range(1+i):
        
        print(d,end=" ")
        d+=1
    print()'''

'''
for x in range(5):

    for k in range(5-x):
        print("*",end=" ")
    print()'''

import time
for i in range(10):
    time.sleep(0.2)
    print('Yo')

for rows in range(10):
    for spaces in range(10-rows):
        print(end=" ")
    for stars in range(rows):
        print(chr(65),end=" ")
    print()
print('--------------------------------------------------------------')
for spaces in range(10):
    for rows in range(10-spaces):
        print('*',end="")
    for stars in range(spaces):
        print(end="")
    print()
print('--------------------------------------------------------------')
A=65
for i in range(10):
    for j in range(i+1):
        print(chr(A),end="")
        A+=1
    print()
print('--------------------------------------------------------------')
A=65
for i in range(10):
    for j in range(i+1):
        print(chr(A),end="")
    A+=1
    print()
print('---------------------------------------------------------------')
for i in range(5):
    for j in range(i+1):
        print(end=" ")
    for s in range(5-i):
        print('*',end=" ")
    print()
print('---------------------------------------------------------------')
B=90
for i in range(5):
    for j in range(i+1):
        print(end=" ")
    for s in range(5-i):
        print(chr(B),end=" ")
    B-=1
    print()

