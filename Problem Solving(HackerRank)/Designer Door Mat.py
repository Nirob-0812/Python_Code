value=input()
size,colmn=map(int,value.split())
c="-"
m=".|."
for i in range(size//2):
    print((c*(((colmn-3)//2)-i*3))+(i*m)+m+(i*m)+(c*(((colmn-3)//2)-i*3)))
print((c*(size+((size-7)//2)))+"WELCOME"+(c*(size+((size-7)//2))))
for i in range(size//2):
    print((c*(3+i*3))+(((((colmn-9)//2)//3)-i)*m)+m+(((((colmn-9)//2)//3)-i)*m)+(c*(3+i*3)))