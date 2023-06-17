class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def add(self,num):
        real_num=self.real+num.real
        image_num=self.imag+num.imag
        result=Complex(real_num,image_num)
        return result


n1=Complex(5,4)
n3=n1     # we can assign object to another variable
n2=Complex(-4,3)
res=n3.add(n2)
print(res.real)
print(res.imag)
