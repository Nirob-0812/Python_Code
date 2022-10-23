def calculateTurnAroundTime(n,wt,bt,tat):
    for i in range(n):
        tat[i]=wt[i]+bt[i]
def calculateWaitingTime(n,bt,wt,tat):
    wt[0]=0
    for i in range(1,n):
        wt[i]=wt[i-1]+bt[i-1]
    calculateTurnAroundTime(n,wt,bt,tat)

if __name__=="__main__":#Start from here
    Burst_time=[]
    n=int(input("How many process do you want: "))
    for i in range(n):
        b=int(input(f"Burst  time for Process {i+1}: "))
        Burst_time.append(b)
    waiting_time=[0]*n
    turnAroundTime=[0]*n
    totalWaitingTime=0
    totalTurnAroundTime=0
    calculateWaitingTime(n,Burst_time,waiting_time,turnAroundTime)
    for i in range(n):
        totalWaitingTime+=waiting_time[i]
    for i in range(n):
        totalTurnAroundTime+=turnAroundTime[i]
    for i in range(n):
        if i==0:
            print("Process | Burst_Time | Waiting_Time | Turn_Around_Time")
        print(f"{i+1}\t\t\t  ->  {Burst_time[i]}\t\t  ->  {waiting_time[i]}\t\t  ->  {turnAroundTime[i]}")
    print("\nTotal Waiting Time: ",totalWaitingTime)
    print("Average Waiting Time: ",totalWaitingTime/n)
    print("Total Turn Around Time: ",totalTurnAroundTime)
    print("Average Turn Around Time: ",totalTurnAroundTime/n)
