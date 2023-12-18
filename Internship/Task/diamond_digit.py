length=int(input("Enter Length:"))
count=1
for i in range(length):
    if count<4:
        print(" "*(length-i)+str(2**count)*i+str(2**count)*(i+1))
    else:
        digit_len=len(str(2**count)*i)+len(str(2**count)*(i+1))
        calculate_len =digit_len-(i+i+1)
        digit=str(2**count)*i+str(2**count)*(i+1)
        print(" "*(length-i)+digit[:-calculate_len])
    count+=1
# print("count:", count)
for i in range(length-2,-1,-1):
    if count<4:
        print(" "*(length-i)+str(2**count)*i+str(2**count)*(i+1))
    else:
        digit_len=len(str(2**count)*i)+len(str(2**count)*(i+1))
        calculate_len =digit_len-(i+i+1)
        digit=str(2**count)*i+str(2**count)*(i+1)
        print(" "*(length-i)+digit[:-calculate_len])
    count+=1