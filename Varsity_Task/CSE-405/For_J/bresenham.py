import matplotlib.pyplot as plt

x1,y1=2,6
x2,y2=7,9
dx=x2-x1
dy=y2-y1
p=2*dy-dx
x=float(x1)
y=float(y1)
x_cordinate=[]
y_cordinate=[]
while(x<=x2):
    x_cordinate.append(x)
    y_cordinate.append(y)
    x+=1
    if p<0:
        y=y
        p=p+2*dy
    elif p>=0:
        y+=1
        p=p+2*dy-2*dx

plt.plot(x_cordinate,y_cordinate,marker="o",color="green")
plt.show()
