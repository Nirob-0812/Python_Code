guess_number=5
guess_count=0
guess_time=3
while guess_count<guess_time:
    guess=int(input("Guess: "))
    if(guess==guess_number):
        print("You Won!")
        break
    guess_count+=1
else:
    print("Sorry, You Failed!")


