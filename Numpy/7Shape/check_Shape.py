import numpy as np

#the first dimension has 2 elements and the second has 4
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)

arr1=np.array([[1,2,3,4],[5,6,7,8]],ndmin=4)
print(arr1)
print(arr1.shape)