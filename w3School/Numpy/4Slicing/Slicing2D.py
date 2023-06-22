import numpy as np

arr=np.array([[1,2,3,4],[5,6,7,8]])
print("Print first Row with slice 3 step:",arr[0,::3])
print("Print first Row with slice 3 step:",arr[0:2,:2])
print("Print from first array 1-3 element: ",arr[0,1:4])
print("Print from both array 1-3 element: ",arr[0:2,1:4])
