def solve(s):
    name=[]
    is_true=False
    for i,c in enumerate(s):
        if i==0:
            name.append(c.upper())
            continue
        if is_true==True:
            name.append(c.upper())
            is_true=False
        elif c.isspace() and s[i+1].islower():
            name.append(c)
            is_true=True
        else:
            name.append(c)
    return "".join(name)

if __name__=="__main__":
    s=input()
    result=solve(s)
    print(result)
