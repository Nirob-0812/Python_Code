import numpy as np

arr=np.array([34,62,42,134,25,30])
filter=[]
for element in arr:
    if element>40:
        filter.append(True)
    else:
        filter.append(False)
print(arr)
print(filter)
print(arr[filter])

