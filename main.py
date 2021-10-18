import datetime
import webbrowser
import time
from pynput import keyboard
from pynput.keyboard import Key,Controller
keyboard=Controller()

def add_data(day):
    hr=input("Enter the hour of the class:")
    mn=input("Enter the minute of the class:")
    lk=input("Enter the link of the class:")
    with open(day,"a") as f:
        f.write(hr+" "+mn+" "+lk+"\n")
    choice=int(input("1:Enter Again\n2:Main Menu\n"))
    if choice==1:
        add_data(day)
    elif choice==2:
        main()

def remove_data(day):
    with open(day,"r") as f:
        print(f.read())
        f.seek(0)
        d = f.readlines()
    ln=int(input(("Which no. link do you want to delete?")))
    '''choice to not delete anything, it was deleting last value(-1) otherwise'''
    if ln==0:
        print("No link deleted")
        main()
    with open(day,"w") as f:
        omit=d[ln-1]
        for i in d:
            if i!=omit:
                f.write(i)
    choice=int(input("1:Remove Again\n2:Main Menu\n"))
    if choice==1:
        remove_data(day)
    elif choice==2:
        main()


def show_data(day):
    with open(day,"r") as f:
        print(f.read())
    input("Enter to continue")
    main()

def work():
    #finding today's day
    now=datetime.datetime.now()
    today=(now.strftime("%A")+".txt").lower()

    '''no. of links on that particular day and assigning values for classtime and links'''
    try:
        with open(today,"r") as f:
                lst=f.read().split("\n")
                cnt=len(lst) 
                f.seek(0)
                link=[None]*cnt
                classtime=[None]*cnt
                for i in range(cnt):
                    val=f.readline().split()
                    classtime[i]=now.replace(hour=int(val[0]),minute=int(val[1]),second=0)
                    link[i]=val[2]
                val=None
    except:
        print("No meetings exist today")
        main()
    '''Finding the starting class'''   
    now=datetime.datetime.now()
    for i in range(cnt):
        if(classtime[i]>now):
            break
    loop=i
    delay=classtime[loop]-now
    print("Time before next link is opened ",delay)
    time.sleep(delay.total_seconds())
    
    while loop<cnt:
        now=datetime.datetime.now()
        '''This is to close zoom is a meeting is already running
        while the next link is being opened'''
        if(now>classtime[loop]):
            if loop: 
                '''to check if it's first meeting as it would
                not require a previous meeting to be closed
                loop==cnt when 48 is implemented'''
                keyboard.press(Key.alt)
                keyboard.press('q')
                time.sleep(0.5)
                keyboard.release(Key.alt)
                keyboard.release('q')
                time.sleep(1)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(1)
            webbrowser.open(link[loop])
            if cnt-loop!=1: 
                delay=classtime[loop+1]-classtime[loop]
                print("Link ",loop+1," executed")
                print("Time before next linked is opened ",delay)
                time.sleep(delay.total_seconds())
            loop+=1
    print("All meetings done for the day")
    input()
    main()   

def main():
    print('''1:Execute scheduled links of the day
    \b\b\b\b2:Add links to a day
    \b\b\b\b3:Remove links from a day
    \b\b\b\b4:Show all links of a day
    \b\b\b\b5:Quit''')
    choice=int(input())
    if choice==1:
        work()
    elif choice==2:
        day=input("Which day?")
        day+=".txt"
        add_data(day.lower())
    elif choice==3:
        day=input("Which day?")
        day+=".txt"
        remove_data(day.lower())
    elif choice==4:
        day=input("Which day?")
        day+=".txt"
        show_data(day.lower())
    elif choice==5:
        quit()
    else:
        print("Wrong option! Choose again")
        main()

main()
