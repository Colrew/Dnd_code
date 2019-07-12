# import tkinter files
from tkinter import *

#loads timer function
import time

#inport Sound
import winsound

#global variables 
it=[1]
mylist=[]
stop=[0]
new=[0]

#funtions

#change window
def chng_frame(frame):
    frame.tkraise()

#creates List of ones for alive
def onelistmaker(n):
    listofones = [1] * n
    return listofones

#Create a list of Player    
def start_list():
    #rest list
    myList=["Top"]
    del myList[:]
    myList=["Top"]
    #Create List of Players
    if tim.get()==1:
        myList.extend(["Spencer"])
    if sut.get()==1:
        myList.extend(["Deb"])
    if tan.get()==1:
        myList.extend(["Moniek"])
    if aul.get()==1:
        myList.extend(["Taylor"])
    if myr.get()==1:
        myList.extend(["Skyler"])
    if bad.get()==1:
        myList.extend(["Tyler"])
##    if fi.get()==1:
##        myList.extend([""])
##    if er.get()==1:
##        myList.extend([""])
    mon=mon_num.get()
    #Create Enemies
    if mon > 25:
        mon=25
    new[0]=mon
    for i in range(mon):
        string= "Enemy_"
        string +=str(i+1)
        myList.extend([string])
    #check list lenght
    Label(monstnum, bg="grey",font= "times 30" , width=20).place(relx=.65, rely=.7,anchor="center")
    if len(myList)<=2:
        chng_frame(monstnum)
        Label(monstnum, bg="grey",font= "times 30" , text = 'Enter More Participants').place(relx=.65, rely=.7,anchor="center")
        return 0
    chng_frame(init)
    #Create Input Grid
    i=len(myList)
    j=(1)
    i -=1
    while i>0:   
        Label(init, font="time 10", relief=RIDGE,width=15, text = myList[j]).grid(row=j, column=0)
        i -=1
        j +=1
    Label(init, font="time 20", relief=RIDGE,width=10, text = myList[0]).grid(row=0, column=0)
    Label(init, font="time 20", relief=RIDGE,width=10, text = "Initiative").grid(row=0, column=1)
    k=35-j
    cover.grid(row=j, column=1)
    while j < 35:
        Label(init, font="time 10", bg="grey",width=15, text=" ").grid(row=j, column=0)
        j+=1
    #Create Global list of people 
    global mylist
    mylist=myList
    n=len(myList)
    #Create Global alive tracker
    global alive
    alive=onelistmaker(n)

#Sort Players Based on Initiative
def sort_init():
    i=len(mylist)
    init=[50]
    i-=1
    #Get Initiative
    if i>0:
        init.extend([numlist1.get()])
        i-=1
    if i>0:
        init.extend([numlist2.get()])
        i-=1
    if i>0:
        init.extend([numlist3.get()])
        i-=1
    if i>0:
        init.extend([numlist4.get()])
        i-=1
    if i>0:
        init.extend([numlist5.get()])
        i-=1
    if i>0:
        init.extend([numlist6.get()])
        i-=1
    if i>0:
        init.extend([numlist7.get()])
        i-=1
    if i>0:
        init.extend([numlist8.get()])
        i-=1
    if i>0:
        init.extend([numlist9.get()])
        i-=1
    if i>0:
        init.extend([numlist10.get()])
        i-=1
    if i>0:
        init.extend([numlist11.get()])
        i-=1
    if i>0:
        init.extend([numlist12.get()])
        i-=1
    if i>0:
        init.extend([numlist13.get()])
        i-=1
    if i>0:
        init.extend([numlist14.get()])
        i-=1
    if i>0:
        init.extend([numlist15.get()])
        i-=1
    if i>0:
        init.extend([numlist16.get()])
        i-=1
    if i>0:
        init.extend([numlist17.get()])
        i-=1
    if i>0:
        init.extend([numlist18.get()])
        i-=1
    if i>0:
        init.extend([numlist19.get()])
        i-=1
    if i>0:
        init.extend([numlist20.get()])
        i-=1
    if i>0:
        init.extend([numlist21.get()])
        i-=1
    if i>0:
        init.extend([numlist22.get()])
        i-=1
    if i>0:
        init.extend([numlist23.get()])
        i-=1
    if i>0:
        init.extend([numlist24.get()])
        i-=1
    if i>0:
        init.extend([numlist25.get()])
        i-=1
    if i>0:
        init.extend([numlist26.get()])
        i-=1
    if i>0:
        init.extend([numlist27.get()])
        i-=1
    if i>0:
        init.extend([numlist28.get()])
        i-=1
    if i>0:
        init.extend([numlist29.get()])
        i-=1
    if i>0:
        init.extend([numlist30.get()])
        i-=1
    if i>0:
        init.extend([numlist31.get()])
        i-=1
##    if i>0:
##        init.extend([numlist32.get()])
##        i-=1
##    if i>0:
##        init.extend([numlist33.get()])
##        i-=1
    #Sort List by inititative 
    j=len(mylist)
    k=40
    bord=["Top"]
    #Create Global Initiative List
    global addnew
    addnew=[50]
    #Sort List and Initiative 
    while k>=0:
        l=1
        while l<j:
            if init[l]==k:
                bord.extend([mylist[l]])
                addnew.extend([init[l]])
            l+=1   
        k-=1
    #Create Global Sorted list 
    global final
    final=bord
    #Create Turn Display
    Label(battle, bg="blue", font="time 50",width=10, text =bord[0]).place(relx=.3, rely=.5, anchor="center")
    Label(battle, bg="yellow", font="time 50",width=10, text =final[1]).place(relx=.7, rely=.5, anchor="center")
    #Cover Battle Message
    Label(battle, bg="grey", font="time 30",width=8, text =(" ")).place(relx=.54, rely=.8, anchor="center")
    Label(battle, bg="grey", font="time 30",width=8, text =(" ")).place(relx=.46, rely=.8, anchor="center")
    chng_frame(battle)
    it[0]=1

#Displays Next Alives turn and the one after
def nextp():
    c=1
    i=it[0]
    #test for top
    if i==0:
        Label(battle, bg="blue", font="time 50",width=10, text =final[0]).place(relx=.3, rely=.5, anchor="center")
        l=1
    #Find Next Alive or back to top
        while l>=1:
            if i==len(final)-l:
                Label(battle, bg="blue", font="time 50",width=10, text =final[0]).place(relx=.7, rely=.5, anchor="center")
                l=0
            elif alive[l]==1:
                m=final[l]
                Label(battle, bg="yellow", font="time 50",width=10, text =m).place(relx=.7, rely=.5, anchor="center")
                l=0
            else:
                l+=1                        
    else:
        k=0
    #test after top for alive
        while k==0:
            if alive[i]==1:
                Label(battle, bg="purple", font="time 50",width=10, text =final[i]).place(relx=.3, rely=.5, anchor="center")
                l=1
    #Find Next Alive or back to top
                while l>=1:
                    if i==len(final)-l:
                        Label(battle, bg="blue", font="time 50",width=10, text =final[0]).place(relx=.7, rely=.5, anchor="center")
                        l=0
                        it[0]=0
                        return 0
                    elif alive[i+l]==1:
                        m=l+i
                        Label(battle, bg="yellow", font="time 50",width=10, text =final[m]).place(relx=.7, rely=.5, anchor="center")
                        l=0
                    else:
                        l+=1
                k=1
            else:
                if i>=len(final)-1:
                    Label(battle, bg="blue", font="time 50",width=10, text =final[0]).place(relx=.7, rely=.5, anchor="center")
                    k=1
                else:
                    gr=i+1
                    it[0]=gr
                    i=it[0]
    #Set to next player
    j=len(final)-1
    if i<j:
        gr=i+1
        it[0]=gr
    if i==j:
        it[0]=0
        
#Adds Enemy, alive and Initiative to List
def add_enemy():
    new[0]+=1
    i=0
    while i <= len(final):
    #Test for end of List
        if i==len(final):
            string= "Enemy_"
            string +=str(new[0])
            final.extend([string])
            t=newinit.get()
            addnew.insert(i,t)
            alive.insert(i,1)
            i=len(final)+1
    #find Location
        elif newinit.get()> addnew[i]:
            string= "Enemy_"
            string +=str(new[0])
            final.insert(i,string)
            addnew.insert(i,newinit.get())
            alive.insert(i,1)
            i=len(final)+1
        else:
            i+=1
    it[0]-=1
    nextp()
    #Create Battle Message
    Label(battle, bg="grey", font="time 30",width=8, text =("joined")).place(relx=.54, rely=.8, anchor="center")
    Label(battle, bg="grey", font="time 30",width=8, text =(string)).place(relx=.46, rely=.8, anchor="center")

#Change Kill list for typed name
def kill():
    i=len(final)-1
    testname=kill_name.get()
    while i>0:
        if testname==final[i]:
            alive[i]=0
            it[0]-=1
            nextp()
    #Create Battle Message
            Label(battle, bg="grey", font="time 30",width=8, text =("killed")).place(relx=.54, rely=.8, anchor="center")
            Label(battle, bg="grey", font="time 30",width=8, text =(final[i])).place(relx=.46, rely=.8, anchor="center")
            i=0
        else:
            i-=1

#Timer funtions        
def start_time ():
    j=30
    Label(battle, font="time 60", width=4 ,text = j).place(relx=.9, rely=.2, anchor="center")
    while j >= 0:
        if stop[0] == 1:
            j=0
            stop[0]=0
            return 0
        wait(j)
        j-=1
    #playes sound at 0
        if j<0:
            duration = 2000  # millisecond
            freq = 600  # Hz
            winsound.Beep(freq, duration)

def stop_time ():
    stop[0]=1

def wait(j):
    Label(battle, font="time 60", width=4 ,text = j).place(relx=.9, rely=.2, anchor="center")
    root.update()
    #waits 1 second
    if j!=0:
        time.sleep(.25)
        root.update()
        time.sleep(.25)
        root.update()
        time.sleep(.25)
        root.update()
        time.sleep(.25)
        root.update()

# create window object
root = Tk()
root.geometry("1920x1080")
root.title('D and D Battles')

# differnet layers
start = Frame(root, width=1920, height=1080, background="grey")
monstnum = Frame(root, width=1920, height=1080, background="grey")
init = Frame(root, width=1920, height=1080, background="grey")
battle = Frame(root, width=1920, height=1080, background="grey")
finish = Frame(root, width=1920, height=1080, background="grey")

#move lavyer to top
for frame in (start, monstnum, init, battle, finish):
      frame.grid(row=0,column=0, stick='news')

#Entry variables
    #Humans Initiative
tim = IntVar()
sut = IntVar()
tan = IntVar()
myr = IntVar()
aul = IntVar()
bad = IntVar()
##fi = IntVar()
##er = IntVar()
    #Number of Enemies 
mon_num = IntVar()
    #New Enemy Initiative
newinit=IntVar()
    #Enemy Initiative
numlist1=IntVar()
numlist2=IntVar()
numlist3=IntVar()
numlist4=IntVar()
numlist5=IntVar()
numlist6=IntVar()
numlist7=IntVar()
numlist8=IntVar()
numlist9=IntVar()
numlist10=IntVar()
numlist11=IntVar()
numlist12=IntVar()
numlist13=IntVar()
numlist14=IntVar()
numlist15=IntVar()
numlist16=IntVar()
numlist17=IntVar()
numlist18=IntVar()
numlist19=IntVar()
numlist20=IntVar()
numlist21=IntVar()
numlist22=IntVar()
numlist23=IntVar()
numlist24=IntVar()
numlist25=IntVar()
numlist26=IntVar()
numlist27=IntVar()
numlist28=IntVar()
numlist29=IntVar()
numlist30=IntVar()
numlist31=IntVar()
numlist32=IntVar()
numlist33=IntVar()

#Entry boxes
    #select players
Checkbutton(monstnum, font= "times 30" , text="Spencer", variable=tim , bg= "grey").place(relx=.3, rely=.4)
Checkbutton(monstnum, font= "times 30" , text="Deb", variable=sut , bg= "grey").place(relx=.3, rely=.5)
Checkbutton(monstnum, font= "times 30" , text="Moniek", variable=tan , bg= "grey").place(relx=.3, rely=.6)
Checkbutton(monstnum, font= "times 30" , text="Taylor", variable=myr , bg= "grey").place(relx=.4, rely=.6)
Checkbutton(monstnum, font= "times 30" , text="Skyler", variable=aul , bg= "grey").place(relx=.4, rely=.4)
Checkbutton(monstnum, font= "times 30" , text="Tyler", variable=bad , bg= "grey").place(relx=.4, rely=.5)
#Checkbutton(monstnum, font= "times 30" , text="Fjord", variable=fi , bg= "grey").place(relx=.3, rely=.7)
#Checkbutton(monstnum, font= "times 30" , text="Erik", variable=er , bg= "grey").place(relx=.4, rely=.7)
    #Number of Enemies
Entry(monstnum,font= "times 25" , textvariable= mon_num).place(relx=.65, rely=.5,anchor="center")
    #New Enemy Initiative
Entry(battle,font= "Times 30", width=5,textvariable=newinit).place(relx=.8, rely=.7, anchor="center")
    #Name to be Killed
kill_name=Entry(battle,font= "Times 30", width=15)
kill_name.place(relx=.2, rely=.7, anchor="center")
    #Enemy Initiative
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist1).grid(row=1, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist2).grid(row=2, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist3).grid(row=3, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist4).grid(row=4, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist5).grid(row=5, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist6).grid(row=6, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist7).grid(row=7, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist8).grid(row=8, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist9).grid(row=9, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist10).grid(row=10, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist11).grid(row=11, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist12).grid(row=12, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist13).grid(row=13, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist14).grid(row=14, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist15).grid(row=15, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist16).grid(row=16, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist17).grid(row=17, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist18).grid(row=18, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist19).grid(row=19, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist20).grid(row=20, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist21).grid(row=21, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist22).grid(row=22, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist23).grid(row=23, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist24).grid(row=24, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist25).grid(row=25, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist26).grid(row=26, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist27).grid(row=27, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist28).grid(row=28, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist29).grid(row=29, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist30).grid(row=30, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist31).grid(row=31, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist32).grid(row=32, column=1)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist33).grid(row=33, column=1)

#Labels
    #Titles
Label(start, bg="grey", font="time 150", text = 'D and D Battles').place(relx=.5, rely=.25, anchor="center")
Label(monstnum, bg="grey", font="time 150", text = 'Select Participants').place(relx=.5, rely=.2, anchor="center")
Label(init, bg="grey", font="time 150", text = 'Enter Initiative').place(relx=.6, rely=.25, anchor="center")
Label(battle, bg="grey", font="time 150", text = 'Players Turn').place(relx=.5, rely=.2, anchor="center")
Label(finish, bg="grey", font="time 150", text = 'End of Battle ').place(relx=.5, rely=.25, anchor="center")
    #Monster Numbers
Label(monstnum, bg="grey",font= "times 30" , text = 'Enter number of Enemies').place(relx=.65, rely=.4,anchor="center")
Label(monstnum, bg="grey",font= "times 30" , text = 'Select Players').place(relx=.4, rely=.35,anchor="center")
    #Battle 
Label(battle, bg="grey", font="time 50",width=10, text =("Current")).place(relx=.3, rely=.4, anchor="center")
Label(battle, bg="grey", font="time 50",width=10, text =("On Deck")).place(relx=.7, rely=.4, anchor="center")
Label(battle, bg="grey", font="time 30", text =("New Enemy Initiative")).place(relx=.8, rely=.65, anchor="center")
    #Timer
Label(battle, font="time 60", width=4 ,text = 30).place(relx=.9, rely=.2, anchor="center")
    #Covers
cover=Label(init, bg="grey",width=15, height=50,)
cover.grid(row=1, column=1 , rowspan=40)

# buttons
    #movemnt between windows 
Button(start, font="times 30 bold", text = 'Start Battle',command = lambda:chng_frame(monstnum), bg='green').place(relx=.5, rely=.6, anchor="center")
Button(monstnum, font="times 30 bold", text = 'Continue',command = lambda:start_list(), bg='green').place(relx=.65, rely=.6, anchor="center")
Button(init, font="times 30 bold", text = 'Begin Turns',command = lambda:sort_init(), bg='green').place(relx=.6, rely=.6, anchor="center")
Button(battle, font="times 30 bold", text = 'Finish Battle',command = lambda:chng_frame(finish), bg='green').place(relx=.5, rely=.7, anchor="center")
Button(finish, font="times 30 bold", text = 'Start a New Battle',command = lambda:chng_frame(start), bg='green').place(relx=.5, rely=.6, anchor="center")
Button(finish, font="times 25 bold", text = 'Exit',command = root.destroy, bg='red').place(relx=.5, rely=.7, anchor="center")
    #Battle Buttons
Button(battle, font="times 30 bold", text = 'Next',command = lambda:nextp(), bg='green').place(relx=.5, rely=.5, anchor="center")
Button(battle, font="times 30 bold", text = 'Start Timer',command = lambda:start_time(), bg='green').place(relx=.9, rely=.3, anchor="center")
Button(battle, font="times 30 bold", text = 'Stop Timer',command = lambda:stop_time(), bg='red').place(relx=.9, rely=.1, anchor="center")
Button(battle, font="times 40",command = lambda:kill(), bg="red", text='Kill').place(relx=.2, rely=.8, anchor="center")
Button(battle, font="times 40",command = lambda:add_enemy(), bg="orange", text='Add Enemy').place(relx=.8, rely=.8, anchor="center")

#Start Gui  
chng_frame(start)

#Main Loop
root.mainloop()


