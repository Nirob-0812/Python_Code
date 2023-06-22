import numpy as np

arr=np.array([0.2,3.7,2.5])
arr1=np.array([0,3,2,0])
converted_to_int=arr.astype(int)
converted_to_bool=arr1.astype(bool)


print(arr)
print(converted_to_int)
print(converted_to_bool)
print(arr.dtype)
print(converted_to_int.dtype)
print(converted_to_bool.dtype)