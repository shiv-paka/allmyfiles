'''
import numpy as np

arr=np.array([1,2,3,4,5,6])

print(arr)'''

import numpy as np
'''
arr=np.array([25,63,15,78,1])
print(arr)
arr2= arr+5
print(arr2)
arr4= arr[arr<4]
print(arr4)

arr3= arr[arr>4]
print(arr3)

arr5=np.array([[21,54,65,89,456],[89,7,8,4,56],[45,89,65,122,3]])
print(arr5)
'''

arr1=np.array([6,2,3,4,5])
#             [T F F T T]
arr2=np.array([1,5,2,9,10])
#Its taking the index values man
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

arr4=np.array([[2,5,6,9,4],[9,7,8,4,5],[3,5,2,1,5],[7,9,1,0,3]])
print(arr4**2)
print(arr4[1,1])
print(arr4[0,4])
print(arr4[1:4,2:4])
print(arr4[:3,:3])



import numpy as np
'''
arr=np.array([1,2,3,4,5])
arr1=np.array([6,7,8,9,10]) 
print(arr)
print(arr1)
print(arr+arr1)
print(arr/arr1)
print(arr*arr1)
print(arr//arr1)

arr2=np.array([[12,32,43,23],[21,34,2,56]])
print(arr2.T)
print(arr2.ndim)
print(arr2.shape)
arr3=([[36,7,32,1],[2,4,1,3]])
print(arr3)
print(arr2+arr3)
#print(arr2*arr3)
arr6=np.zeros((3,5))
arr7=arr6*10
print(arr7)

arr8=np.ones((4,5))
arr9=arr8*10
print(arr8)

arr10=np.empty((5,6))
print(arr10)

arr11=np.array([
    [[1,2,3,4,5],
     [6,7,8,9,10]],
     
     [[11,1,3,4,6],
     [12,4,6,8,10]],
      
     [[13,9,23,4,5],
     [56,43,32,4,6]]
    ])
print(arr11)
print(arr11[1,0,3])
print(arr11[1:3,0:2])
print(arr11[1,1,1:]) '''
      


