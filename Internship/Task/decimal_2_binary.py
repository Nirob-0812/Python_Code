def calculate_deci_2_bin(val):
    if(val>1):
        calculate_deci_2_bin(val//2)
    print(val%2,end=" ")

deci=int(input("Enter Decimal Value: "))
calculate_deci_2_bin(deci)