import matplotlib.pyplot as plt

x1,y1=2,6
x2,y2=4,11
dx=x2-x1
dy=y2-y1
step=max(dx,dy)
xinc=dx/step
yinc=dy/step
x=float(x1)
y=float(y1)
x_cordinate=[]
y_cordinate=[]
for i in range(step):
    x_cordinate.append(x)
    y_cordinate.append(y)
    x+=xinc
    y+=yinc

plt.plot(x_cordinate,y_cordinate,marker="o",color='green')
plt.show()