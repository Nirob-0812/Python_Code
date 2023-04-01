if __name__ == '__main__':
    s = input()
    alphaNum=False
    alpha=False
    digit=False
    lower=False
    upper=False
    for i in range(len(s)):
        if (s[i].isalnum()):
            alphaNum=True
        if(s[i].isalpha()):
            alpha=True
        if(s[i].isdigit()):
            digit=True
        if(s[i].islower()):
            lower=True
        if(s[i].isupper()):
            upper=True
    print(alphaNum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)