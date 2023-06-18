def binary_search(list,s,l,u):
    global index
    while l<=u:
        mid=int((l+u)/2)
        if s==list[mid]:
            index=mid
            return True
        else:
            if s>list[mid]:
                l=mid+1
            elif s<list[mid]:
                u=mid-1
    else:
        return False

list=[5,7,10,14,23,34,43,65,85] #0 1 2 3 4 5 6 7 8 9
lower=0
item=85
upper=len(list)-1
if binary_search(list,item,lower,upper):
    print("Found in position:",index+1)
else:
    print("Not Found in the list!")