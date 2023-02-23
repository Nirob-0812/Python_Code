class Nirob:
    def __init__(self):
        print("My name is Nirob")
class Mehedi(Nirob):
    def __init__(self):
        super().__init__()
        print("My name is Mehedi")
p=Mehedi()