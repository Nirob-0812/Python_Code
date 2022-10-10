start=False
start_count=0
stop_count=1

while True:
    get_input=input(">")
    if get_input=="help":
        print("Start - To Start the Car")
        print("Stop - To Stop the Car")
        print("Quit - To Exit")
    elif get_input== "start" and not start and start_count==0:
        print("Car Started...Ready to go..")
        start=True
        start_count+=1
        stop_count=0
    elif get_input== "start" and start and start_count==1:
        print("Car Already Started")
        start_count+=1
    elif get_input== "start" and start and start_count>1:
        print("Hey, What are you doing!.. Car Already Started")
    elif get_input== "stop" and start and stop_count==0:
        print("Car Stopped")
        start=False
        stop_count+=1
        start_count=0
    elif get_input== "stop" and not start and stop_count==1:
        print("Car Alredy Stopped")
        start=False
        stop_count+=1
    elif get_input== "stop" and not start and stop_count>1:
        print("Hey, What are you doing!.. Car Already Stopped")
    elif get_input== "quit":
        break
    else:
        print("Sorry, I don't Understand!")
