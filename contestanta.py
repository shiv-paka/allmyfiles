'''lst=[1,2,3,4,5]
lst1=[]
for i in range(1,len(lst)+1):
    lst1.append(lst[-i])
print(lst1)

lstInp=int(input("Enter the length of list: "))
lst=[]
lst1=[]
for i in range(lstInp):
    listEle=int(input("Enter the element: "))
    lst.append(listEle)
#print(sorted(lst))
lstLen=len(lst)
for j in range(1,lstLen+1):
     lst1.append(sorted(lst[-j]))
print(lst1)
'''
'''
lstInp=int(input())
lst=[]
lst1=[]
for i in range(lstInp):
    listEle=int(input())
    lst.append(listEle)
    
lstLen=len(lst)
for j in range(1,lstLen+1):
     lst1.append(lst[-i])
print(lst1)'''
'''
lstInp=int(input())
lst=[]
lst1=[]
for i in range(lstInp):
    listEle=int(input())
    lst.append(listEle)
    

for i in range(1,lstInp+1):
     lst1.append(lst[-i])
print(lst1)
a=123

sum1=0
for ele in a:
     sum1+=ele
print(sum1)'''
print(len("Hello"))

a=input()

lower=0
upper=0

for ch in a:
   
    ascii=ord(ch)
    if ascii in range(65,91):
        upper+=1
    elif ascii in range(97,122):
        lower+=1
print(f"{upper} uppercase, {lower} lowercase ")