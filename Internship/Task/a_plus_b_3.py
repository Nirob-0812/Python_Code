a,b=map(int,input("Enter Redius, Height by space:").split())
lhs=(a+b)**3
rhs=(a**3)+(b**3)+3*(a**2)*b+3*a*(b**2)
print("Left Side:",lhs)
print("Right Side:",rhs)
if lhs==rhs:
    print("Proved")
