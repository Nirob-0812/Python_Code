import math
class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def calculate_triangle(self):
        sp=(self.a+self.b+self.c)/2
        area=math.sqrt(sp*(sp-self.a)*(sp-self.b)*(sp-self.c))
        return area

triangle=Triangle(3,6,7)
Area=triangle.calculate_triangle()
print("Area of Triangle:","{:.2f}".format(Area))
