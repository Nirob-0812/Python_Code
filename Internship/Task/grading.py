def calculate_grade(mark):
    grade=""
    if(mark<35):
        grade="F"
    elif(mark>35 and mark<39):
        grade = "D"
    elif(mark > 40 and mark < 49):
        grade = "C"
    elif(mark > 50 and mark < 59):
        grade = "C+"
    elif(mark > 60 and mark < 69):
        grade = "B"
    elif(mark > 75 and mark < 79):
        grade = "B+"
    elif(mark > 80 and mark < 89):
        grade = "A"
    elif (mark>= 90):
        grade = "A+"
    return grade

mark=int(input("Enter Your Mark: "))
grad=calculate_grade(mark)
print("Your Grade: ",grad)