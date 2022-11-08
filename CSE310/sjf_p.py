def findWaitningTime(proc,wt,n):
    rt=[0]*n
    for i in range(n):
        rt[i]=proc[i][1]
    complete=0
    iterate=0
    t=0
    minim=999999999
    check=False
    while(complete!=n):
        for j in range(n):
            if ((proc[j][2]<=t) and (rt[j]<minim) and rt[j]>0):
                minim=rt[j]
                iterate=j
                check=True

        if (check==False):
            t+=1
            continue
        rt[iterate]-=1
        minim=rt[iterate]

        if(minim==0):
            minim=999999999
        if(rt[iterate]==0):
            complete+=1
            check=False
            finish=t+1
            wt[iterate]=finish-proc[iterate][1]-proc[iterate][2]
        t+=1

def findTurnAroundTime(proc,wt,tat,n):
    for i in range(n):
        tat[i]=wt[i]+proc[i][1]

def findSjf(proc,n):
    wt=[0]*n
    tat=[0]*n
    findWaitningTime(proc,wt,n)
    findTurnAroundTime(proc,wt,tat,n)
    print("Process | Burst | Arrival | waiting | Turn_Around\n")
    for i in range(n):
        print(f"{proc[i]}\t\t{proc[i][1]}\t\t{proc[i][2]}\t\t{wt[i]}\t\t{tat[i]}")
if __name__=="__main__":
    process=[[1, 6, 1], [2, 8, 1],
            [3, 7, 2], [4, 3, 3]]
    n=4
    findSjf(process,n)