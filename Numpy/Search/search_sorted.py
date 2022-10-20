import numpy as np

arr=np.array([6,8,9,7])
print(np.searchsorted(arr,7))
print(np.searchsorted(arr,7,side='right'))