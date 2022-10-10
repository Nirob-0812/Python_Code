import numpy as np

arr=np.array([1,2,3,4,5,6])
viewed=arr.view()
print("Original: ",arr)
print("viewed: ",viewed)

viewed[2]=8

print("Original after View: ",arr)
print("viewed afer view: ",viewed)