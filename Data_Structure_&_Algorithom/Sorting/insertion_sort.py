list=[6,5,3,7,1,8,0,4,2]

for i in range(1,len(list)):
    for j in range(i-1,-1,-1):
        if list[j+1]<list[j]:
            list[j],list[j+1]=list[j+1],list[j]
    print(list)

print(list)