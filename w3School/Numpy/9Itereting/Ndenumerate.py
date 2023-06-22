import numpy as np

arr=np.array([1,2,3,4,5])
arr1=np.array([[1,2,3,4],[5,6,7,8]])
for index,x in np.ndenumerate(arr):
    print("Index: ",index,"Element: ",x)

for index1,y in np.ndenumerate(arr1):
    print(f"Index: {index1} ELement: ,{y}")