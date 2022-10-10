i=1
k=9
while i<=9:
    if(i==1):
        print(f"{' ' * k}{'*'}")
        k= k - 1
    print(f"{' ' * k}{'*' * 1 * i}{'*' * 1 * i}")
    i+=2-1
    k-=1