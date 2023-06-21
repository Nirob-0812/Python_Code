def selection(list):
    for i in range(len(list)-1):
        min=i
        for j in range(i+1,len(list)):
            if list[min]>=list[j]:
                min=j
        list[i],list[min]=list[min],list[i]
    return list
list=[5,3,9,6,8,3,1,7]
sorted=selection(list)
print(sorted)