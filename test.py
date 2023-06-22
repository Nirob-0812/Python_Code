thikness=4
n="N"
t="T"
ts=thikness
tc=thikness*2
print("\n\n")
for i in range(thikness*4):
    print((n * thikness).ljust(thikness)+("  "*i)+(n*thikness).rjust(thikness)+("  "*((thikness*4)-i-1-ts))+(tc*"T")+((t*thikness) if i==0 else (n*thikness)).ljust(thikness)+(tc*"T"))
    ts=0
    tc=0