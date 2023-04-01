# def print_rangoli(size):
alphabet = 'zyxwvutsrqponmlkjihgfedcba'
size=5
alpha =alphabet[-size:]
for i in range((size*2)-1):
    if i<size:
        string=alpha[:i+1]+alpha[:i][::-1]
    if i>=size:
        string=alpha[:size-i-1]+alpha[:size-i-1][::-1][1:]
    print("-".join(string).center(((size*4)-3),"-"))