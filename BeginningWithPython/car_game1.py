started=False
while True:
    get_input=input("> ")
    if get_input=="help":
        print(
'''Start - To Start the Car
Stop - To Stop the Car
Quit - To Exist''')
    elif get_input=="start":
        if started:
            print("Car is Already Started!")
        else:
            started=True
            print("Car Started")
    elif get_input=="stop":
        if started:
            started=False
            print("Car Stopped")
        else:
            print("Car Already Stopped!")
    elif get_input=="quit":
        break
    else:
        print("Sorry,Don't Understand!")