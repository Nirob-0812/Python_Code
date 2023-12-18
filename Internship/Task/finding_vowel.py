def count_vowel(sen):
    a,e,i,o,u=[0]*5
    for j in sen:
        if j=="a" or j=="A":
            a+=1
        if j=="e" or j=="E":
            e+=1
        if j=="i" or j=="I":
            i+=1
        if j=="o" or j=="O":
            o+=1
        if j=="u" or j=="U":
            u+=1
    if a>0:
        print(f"Total 'A' is: {a}")
    if e>0:
        print(f"Total 'E' is: {e}")
    if i>0:
        print(f"Total 'I' is: {i}")
    if o>0:
        print(f"Total 'O' is: {o}")
    if u>0:
        print(f"Total 'U' is: {u}")



sen=input("Enter Sentence: ")
count_vowel(sen)