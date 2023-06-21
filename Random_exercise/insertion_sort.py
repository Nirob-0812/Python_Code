def insertion_sort(list):
    for i in range(1,len(list)):
        for j in range(i,0,-1):
            if list[j]<list[j-1]:
                list[j-1],list[j]=list[j],list[j-1]
        print(list)
    return list

list=[3,2,1,5,9,2,1,8,4]
sorted=insertion_sort(list)
print(sorted)
