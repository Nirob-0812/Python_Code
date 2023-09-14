import matplotlib.pyplot as plt

input_point=input("Enter Start and End Point:")
split_input=input_point.split()
x1,y1,x2,y2=map(int,split_input) #(1,2) (2,3) (3,4)   (6,7)
dx=abs(x2-x1)
dy=abs(y2-y1)
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


