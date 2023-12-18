length=int(input("Enter Length:"))

for i in range(length-3,length):
    print(" "*(length-i)+"*"*i+"*"*(i+1))
for i in range(length-2,-1,-1):
    print(" "*(length-i)+"*"*i+"*"*(i+1))