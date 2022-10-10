import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
print("Print 2-end:",arr[1:])
print("Print 3-8:",arr[2:8])
print("Print 3-8 by negative slicing:",arr[-7:-1])
print("Print begin-end:",arr[:])
print("Print every 2 step:",arr[::2])
print("Print every 2 step from 4:",arr[3::2])
