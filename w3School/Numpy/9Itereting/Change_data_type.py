import numpy as np

arr=np.array([1,2,3,4,5])

for x in np.nditer(arr,flags=['buffered'],op_dtypes='S'):
    print(x)