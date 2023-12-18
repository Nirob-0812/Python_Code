num=int(input("Enter Number: "))
f=0
s=1
next=s
for i in range(num):
    if i <2:
        print(i,end=" ")
    else:
        print(next, end=" ")
        f,s=s,next
        next=f+s
