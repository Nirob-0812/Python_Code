name=input("Enter your name: ")
length=len(name)
if length <3:
    print("Name must be at least 3 Characters")
elif length >50:
    print("Name can be maximum of 50 Characters")
elif length >=3 and length<=50:
    print("Name looks good!")