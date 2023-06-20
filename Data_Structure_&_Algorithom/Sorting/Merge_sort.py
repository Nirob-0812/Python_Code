def merge_sort(arr):
    if len(arr)<=1:
        return arr
    half_indx=len(arr)//2
    left_arr=arr[:half_indx]
    right_arr=arr[half_indx:]
    left_arr=merge_sort(left_arr)
    right_arr=merge_sort(right_arr)

    merged=merge(left_arr,right_arr)
    return merged

def merge(left,right):
    merged=[]
    left_indx=0
    right_indx=0
    while left_indx<len(left) and right_indx<len(right):
        if left[left_indx]<=right[right_indx]:
            merged.append(left[left_indx])
            left_indx+=1
        else:
            merged.append(right[right_indx])
            right_indx+=1

    merged.extend(left[left_indx:])
    merged.extend(right[right_indx:])
    return merged

arr=[4,6,3,2,9,7,1]
sorted=merge_sort(arr)
print(sorted)