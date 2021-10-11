import datetime
import webbrowser
import time
cnt=int(input("How many classes today?"))
link=[None]*cnt
classtime=[None]*cnt

now=datetime.datetime.now()
for i in range(0,cnt):
    classtime[i]=now.replace(hour=int(input("Enter the hour of the class:")),minute=int(input("Enter the minute of the class:")),second=0)
    link[i]=(input("Enter the link of the class:"))

now=datetime.datetime.now()
delay=classtime[0]-now
print("Time before next linked is opened ",delay)
time.sleep(delay.total_seconds())
loop=0
while loop<cnt:
    now=datetime.datetime.now()
    if(now>classtime[loop]):
        webbrowser.open(link[loop])
        if cnt-loop!=1: 
            delay=classtime[loop+1]-classtime[loop]
            print("Link ",loop+1," executed")
            print("Time before next linked is opened ",delay)
            time.sleep(delay.total_seconds())
        loop+=1   
       