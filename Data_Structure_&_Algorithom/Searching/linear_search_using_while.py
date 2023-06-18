def linear_search(list,n):
    i=0
    global p
    while i<len(list):
        if list[i]==n:
            #globals() ['p']=i
            p=i
            return True
        i+=1
    else:
        return False

list =[3,4,2,5,1,9,0,6,8]
if linear_search(list,8):
    print("Found in position:",p+1)
else:
    print("Not found in the list!")