import datetime
import webbrowser
cnt=int(input("How many classes today?"))
link=[None]*cnt
classtime=[None]*cnt

now=datetime.datetime.now()
for i in range(0,cnt):
    classtime[i]=now.replace(hour=int(input("Enter the hour of the class:")),minute=int(input("Enter the minute of the class:")),second=0)
    link[i]=(input("Enter the link of the class:"))


loop=0
while loop<cnt:
    now=datetime.datetime.now()
    if(now>classtime[loop]):
        webbrowser.open(link[loop])
        loop+=1
        print("link ",loop," executed")
        