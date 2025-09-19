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


