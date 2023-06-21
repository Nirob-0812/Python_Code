def merge_sort(list):
    if len(list)<=1:
        return list
    mid=len(list)//2
    left_list=list[:mid]
    right_list=list[mid:]
    left_list=merge_sort(left_list)
    right_list=merge_sort(right_list)
    merged=merge(left_list,right_list)

    return merged

def merge(left,right):
    merged=[]
    left_indx=0
    right_indx=0
    while left_indx<len(left) and right_indx<len(right):
        if left[left_indx] <= right[right_indx]:
            merged.append(left[left_indx])
            left_indx+=1
        else:
            merged.append(right[right_indx])
            right_indx+=1
    merged.extend(left[left_indx:])
    merged.extend(right[right_indx:])
    return merged
list=[3,2,7,1,8,2,0,4]
sorted=merge_sort(list)
print(sorted)