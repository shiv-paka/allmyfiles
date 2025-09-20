'''
import array as arr
nums=arr.array('i',[])
size=int(input("enter size: "))
for i in range(size):
    nums.append(27)'''

#Blank array creation
import array as arr
'''nums=arr.array('i',[])
size=int(input('Enter the size:'))
for i in range(size):
    ele=int(input('Enter element:'))
    nums.append(ele)
print(nums)'''

import array as ary
numbers=ary.array('i',[])
Size=int(input('Enter the size of the array:'))
summation=0
for i in range(Size):
    element=int(input('Enter element:'))
    numbers.append(element)
    summation=summation+element
print(numbers[::-1])
large=max(numbers)
smol=min(numbers)
print('The largest number is:', large) 
print(f'The smallest number is: {smol}')
print(f'Their sum is: {summation}')

exist=int(input('Enter the value you want to check:'))

for exist in range(len(numbers)):
    

 if exist in numbers:
    print(f'Yes, {exist} exists in {numbers} , it is in  position')
else :
    print(f'No , {exist} does not exist in {numbers}')

#numoy

import numpy as np
'''
arr=np.array([1,2,3,4,5])
print(arr)
arr2= arr+5
print(arr2)
arr4= arr[arr<4]
print(arr4)

arr3= arr[arr>4]
print(arr3)

arr5=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(arr5)'''

arr1=np.array([6,2,3,4,5])
#             [T F F T T]
arr2=np.array([1,5,2,9,10])
#             Its taking the index values man
arr3=arr2[arr1>=4]
print(arr3)


arr5=([6,2,3,4,5,1,5,2,9,10])
print(arr5[1:6])
print(arr5[2])
print(arr5[3])
print(arr5[4])
print(arr5[5])
print(arr5[-8:-5])
print(arr5[-7])
print(arr5[-6])

arra1=np.arange(13)
arra2=np.arange(0,1,13)


arr4=np.array([[2,5,6,9,4],[9,7,8,4,5]])
print(arr4**2)
print(arr4[1,1])
print(arr4[0,4])
print(arr4[1:4,2:4])
print(arr4[:3,:3])

