list=[4,3,6,9,2,1,7]

for i in range(len(list)):
    for j in range(len(list)-1-i):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]

print(list)
