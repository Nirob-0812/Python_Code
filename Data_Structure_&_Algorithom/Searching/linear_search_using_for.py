index=-1

def linear_search(list,n):
    global index
    for i in range(len(list)):
        if list[i]==n:
            index=i
            return True
    else:
        return False

list=[4,0,6,1,3,2,7,9]

if linear_search(list,20):
    print("Found in position:",index+1)
else:
    print("Not Found in the list!")