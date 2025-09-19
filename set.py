#st={1,2,3,4,5}
#print(st)
#st.add(7)
#print(st)
#st.update([8,9,0,12])
#print(st)
##discaard remones the element if it exists in the list or if it doesn't exist then lite.
#st.discard(8)
#print(st)
#st.discard(13)
##clears all elements
#st.clear()
#print(st)
#st2=st
#st3=st.copy()
#print("st3:",st3)
#print()
#st3.add(6)
#print("set1:",st)
#print("set2:",st2)
#print("set3:",st3)

'''import time
for i in  range(10):
    time.sleep(0.4)
    print('very')
    print()
print('sus')''' 

'''set1={1,2,3,4}
set2={2,3,4,5}
print(set1|set2)
print(set1&set2)
print(set1-set2)
print(set1^set2)

for ele in set1:
    print(ele)
print(2 in set2)
print(8 in set2)'''
 
set3={10,20,'H',30,40}
A=0
for elem in set3:
    A+=1
print(A)

lst1=[20,10,12,23,20,10]
empSet=set()
for elem in lst1:
    #empSet.add(elem)
    if (elem in empSet):
     print('No')
     print(empSet)
     break
    else :
       empSet.add(elem)
       print(empSet)
print('======================================================')
empSet1=set()
for i in range(len(lst1)):
   if lst1[i] in empSet1:
      print('No')
   else:
      empSet1.add(lst1[i])
strng="Hello"
stStrng=set()
for i in range(len(strng)):
   stStrng.add(strng[i])
print(sorted(stStrng))

lstNames=['Hello','Welcome','Hi','Welcome']
empSetNames=set()
for elemen in lstNames:
     empSetNames.add(elemen)
print(empSetNames)
