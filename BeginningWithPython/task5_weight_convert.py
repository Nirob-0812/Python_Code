weight=input("Weight: ")
units=input("(L)bs or (K)g: ")
if units=='l':
    print(f"You are {float(weight)*0.45} kilos")
elif units=="k":
    print(f"You are {float(weight)/0.45} pounds")
else:
    print("Please Enter Correct Input")