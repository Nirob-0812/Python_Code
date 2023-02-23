class Triangle:
    def __init__(self,Base,Height):
        self.base=Base
        self.height=Height
    def Calculate(self):
        print(f"Area: {0.5*self.base*self.height}")
t1=Triangle(10,20)
t2=Triangle(20,30)
t1.Calculate()
t2.Calculate()
