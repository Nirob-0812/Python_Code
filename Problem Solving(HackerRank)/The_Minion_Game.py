def minion_game(string):
    str_length=len(string)
    stuart=kevin=0 #banana
    for i in range(str_length):
        if s[i] in "AEIOU":
            kevin+=str_length-i
        else:
            stuart+=str_length-i
    if stuart>kevin:
        print("Stuart",stuart)
    elif stuart<kevin:
        print("Kevin",kevin)
    else:
        print("Draw")    
    

if __name__ == '__main__':
    s = input()
    minion_game(s)