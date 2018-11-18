file = open("input.txt","r")
line=file.readlines()
a=len(line)
file.close()
file = open("input.txt","r")
p=[]
for i in range(a):
    p.append(file.readline())
process=[]
arrival_time=[]
burst_time=[]
waiting_time=[]
turnaround_time=[]
tat=0
wt=0
for i in range(a):
    x , y , z = p[i].split()
    process.append(x)
    arrival_time.append(int(y))
    burst_time.append(int(z))
    waiting_time.append(int(wt))
    tat = int(z)+wt
    turnaround_time.append(int(tat))
    wt+=int(z)
print ("process\t\tarrival_time\tburst_time\twaiting_time\tturnaround_time")
for i in range(a):
    print(process[i] + "\t\t" + str (arrival_time[i]) + "\t\t" + str (burst_time[i]) + "\t\t" + str (waiting_time[i]) + "\t\t" + str (turnaround_time[i] ))
print("Gant Chart: ")
print(str(waiting_time[0]), end = "")
for i in range(a):
    print("******" + str(turnaround_time[i]) + "(" + process[i] + ")", end = "")
print("\n")
avg_wt = 0
avg_tat = 0
sum1 = sum2 = 0
for i in range(a):
    sum1 += waiting_time[i]
    sum2 += turnaround_time[i]
avg_wt = sum1/a
avg_tat = sum2/a
print("Average Waiting time: " + str(avg_wt))
print("Average Turnaround time: " + str(avg_tat))