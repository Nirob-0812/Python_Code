list=[3,8,5,2,9,6,0,6,1]

for i in range(len(list)-1):
    min_position = i
    for j in range(i,len(list)):
        if list[min_position]>list[j]:
            min_position=j
    list[i],list[min_position]=list[min_position],list[i]
    print(list)

print(list)