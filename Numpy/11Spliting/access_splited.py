import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
newarr=np.array_split(arr,3)

for j in newarr:
    print(j)