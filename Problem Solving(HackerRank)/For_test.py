def minion_game(string):
    # your code goes here
    str_length = len(string)
    sum_K=sum_S=0
    for i in range(0,str_length):
        if string[i] in 'AEIOU':
            sum_K += str_length - i
        else:
            sum_S += str_length - i
    if sum_S > sum_K:
        print("Stuart",sum_S)
    elif sum_K > sum_S:
        print("Kevin",sum_K)
    else:
        print("Draw")


if __name__=="__main__":
    minion_game("BANANA")