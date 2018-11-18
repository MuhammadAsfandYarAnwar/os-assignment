file = open ("input.txt","r")
line=file.readlines()
print(line)
n=len(line)
process=[]
burst_time=[]
priority=[]
for i in range(n):
    x , y , z = line[i].split(" ")
    process.append(x)
    burst_time.append(int(y))
    priority.append(int(z))
print(process)
turn_around_time=[]
waiting_time=[]
for i in range(0,len(priority)-1):
    for j in range(0,len(priority)-i-1):
        if(priority[j]>priority[j+1]):
            temp=priority[j]
            priority[j]=priority[j+1]
            priority[j+1]=temp
            temp=burst_time[j]
            burst_time[j]=burst_time[j+1]
            burst_time[j+1]=temp
            temp=process[j]
            process[j]=process[j+1]
            process[j+1]=temp
 
waiting_time.insert(0,0)
turn_around_time.insert(0,burst_time[0])
for i in range(1,len(process)):
     waiting_time.insert(i,waiting_time[i-1]+burst_time[i-1])
     turn_around_time.insert(i,waiting_time[i]+burst_time[i])
 

avg_turn_around_time=0
avg_waiting_time=0
for i in range(0,len(process)):
     avg_waiting_time=avg_waiting_time+waiting_time[i]
     avg_turn_around_time=avg_turn_around_time+turn_around_time[i]
     avg_waiting_time=float(avg_waiting_time)/n
     avg_waiting_time=float(avg_turn_around_time)/n
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for i in range(0,n):
     print(str(process[i])+"\t\t"+str(burst_time[i])+"\t\t"+str(waiting_time[i])+"\t\t"+str(turn_around_time[i]))
print("Gant Chart: ")
print(str(waiting_time[0]), end = "")
for i in range(n):
    print("******" + str(turn_around_time[i]) + "(" + process[i] + ")", end = "")
print("\n")
print("Average Waiting time is: "+str(avg_waiting_time))
print("Average Turn Around Time is: "+str(avg_turn_around_time))