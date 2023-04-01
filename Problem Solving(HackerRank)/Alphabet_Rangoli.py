def print_rangoli(size):
    alphabet = 'zyxwvutsrqponmlkjihgfedcba'
    alpha =alphabet[-size:]
    for i in range((size*2)-1):
        if i<size:
            string=alpha[:i+1]+alpha[:i][::-1]
        if i>=size:
            string=alpha[:size-i-1]+alpha[:size-i-1][::-1][1:]
        print("-".join(string).center(((size*4)-3),"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)