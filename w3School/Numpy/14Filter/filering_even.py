import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
filter=arr%2==0
print(filter)
newarr=arr[filter]
print(newarr)