import numpy as np
import matplotlib.pyplot as plt

list=[86,87,88,86,87,85,86]
list2=[32,111,138,28,59,77,97]
print("low standard deviaiton:",np.std(list))
print("high standard deviaiton:",np.std(list2))

plt.plot(list,list2,marker="o",color='green')
plt.show()