def turnAround(proc,wt,tat,n):
    for i in range(n):
        tat[i]=wt[i]+proc[i][1]

def findWaiting(proc,wt,n):
    wt[0]=0
    for i in range(1,n):
        wt[i]=proc[i-1][1]+wt[i-1]

def findAvg(proc,n):
    wt=[0]*n
    tat=[0]*n
    findWaiting(proc,wt,n)
    turnAround(proc,wt,tat,n)
    for i in range(n):
        print(proc[i][1]," ",wt[i]," ",tat[i]," ")
def findPriority(proc,n):
    proc=sorted(proc,key=lambda proc: proc[2], reverse=True)
    print("Shorted list which will executed:")
    for i in proc:
        print(i[0]," ")
    findAvg(proc,n)

if __name__=="__main__":
    proc=[[1, 10, 1],
            [2, 5, 0],
            [3, 8, 1]]
    n=3
    findPriority(proc,n)
