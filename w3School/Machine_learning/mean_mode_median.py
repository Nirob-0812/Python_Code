import numpy as np
from scipy import stats
data=[99,86,87,88,111,86,103,87,94,78,77,85,87,86]
std_data=[4, 2, 5, 8, 6]
mean=np.mean(data)
median=np.median(data)
mode=stats.mode(data)
standard_dev=np.std(std_data)
print("Mean:",mean)
print("Median:",median)
print("Mode:",mode)
print("Standard Deviation:",standard_dev)