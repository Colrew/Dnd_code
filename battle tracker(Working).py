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
hp=[0]

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
    Label(init, font="time 20", relief=RIDGE,width=10, text = "HP").grid(row=0, column=2)
    k=35-j
    cover.grid(row=j, column=1)
    cover4.grid(row=j, column=2)
    while j < 35:
        Label(init, font="time 10", bg="grey",width=15, text=" ").grid(row=j, column=0)
        j+=1
        
    #Create battle List
    i=len(myList)
    j=(1)
    i -=1
    while i>0:   
        Label(battle, font="time 10", relief=RIDGE,width=10, text = myList[j]).grid(row=j, column=0)
        i -=1
        j +=1
    Label(battle, font="time 10", relief=RIDGE,width=10, text = myList[0]).grid(row=0, column=0)
    Label(battle, font="time 10", relief=RIDGE,width=10, text = "Description").grid(row=0, column=1)
    Label(battle, font="time 10", relief=RIDGE,width=5, text = "HP").grid(row=0, column=2)
    Label(battle, font="time 10", relief=RIDGE,width=5, text = "Damage").grid(row=0, column=3)
    k=35-j
    cover2.grid(row=j, column=1)
    cover3.grid(row=j, column=3)
    while j < 35:
        Label(battle, font="time 10", bg="grey",width=15, text=" ").grid(row=j, column=0)
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
    i=len(final)
    global hp
    hp=[50]
    i-=1
    #Get HP
    if i>0:
        hp.extend([hplist1.get()])
        i-=1
    if i>0:
        hp.extend([hplist2.get()])
        i-=1
    if i>0:
        hp.extend([hplist3.get()])
        i-=1
    if i>0:
        hp.extend([hplist4.get()])
        i-=1
    if i>0:
        hp.extend([hplist5.get()])
        i-=1
    if i>0:
        hp.extend([hplist6.get()])
        i-=1
    if i>0:
        hp.extend([hplist7.get()])
        i-=1
    if i>0:
        hp.extend([hplist8.get()])
        i-=1
    if i>0:
        hp.extend([hplist9.get()])
        i-=1
    if i>0:
        hp.extend([hplist10.get()])
        i-=1
    if i>0:
        hp.extend([hplist11.get()])
        i-=1
    if i>0:
        hp.extend([hplist12.get()])
        i-=1
    if i>0:
        hp.extend([hplist13.get()])
        i-=1
    if i>0:
        hp.extend([hplist14.get()])
        i-=1
    if i>0:
        hp.extend([hplist15.get()])
        i-=1
    if i>0:
        hp.extend([hplist16.get()])
        i-=1
    if i>0:
        hp.extend([hplist17.get()])
        i-=1
    if i>0:
        hp.extend([hplist18.get()])
        i-=1
    if i>0:
        hp.extend([hplist19.get()])
        i-=1
    if i>0:
        hp.extend([hplist20.get()])
        i-=1
    if i>0:
        hp.extend([hplist21.get()])
        i-=1
    if i>0:
        hp.extend([hplist22.get()])
        i-=1
    if i>0:
        hp.extend([hplist23.get()])
        i-=1
    if i>0:
        hp.extend([hplist24.get()])
        i-=1
    if i>0:
        hp.extend([hplist25.get()])
        i-=1
    if i>0:
        hp.extend([hplist26.get()])
        i-=1
    if i>0:
        hp.extend([hplist27.get()])
        i-=1
    if i>0:
        hp.extend([hplist28.get()])
        i-=1
    if i>0:
        hp.extend([hplist29.get()])
        i-=1
    if i>0:
        hp.extend([hplist30.get()])
        i-=1
    if i>0:
        hp.extend([hplist31.get()])
        i-=1
##    if i>0:
##        hp.extend([hplist32.get()])
##        i-=1
##    if i>0:
##        hp.extend([hplist33.get()])
##        i-=1
        #show hp
    i=len(final)
    j=(1)
    i -=1
    while i>0:   
        Label(battle, font="time 10", relief=RIDGE,width=5, text = hp[j]).grid(row=j, column=2)
        i -=1
        j +=1

    

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
    Label(battle, font="time 10", relief=RIDGE,width=10, text = string).grid(row=len(final)-1, column=0)
    #move Cover
    cover2.grid(row=len(final), column=1)
    cover3.grid(row=len(final), column=3)
    #add hp
    hp.extend([hpnew.get()])
    Label(battle, font="time 10", relief=RIDGE,width=5, text = hp[(len(final)-1)]).grid(row=len(final)-1, column=2)


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

# do Damage
def dodamage():
    i=len(final)
    hurt=[0]
    i-=1
    #Get HP
    if i>0:
        hurt.extend([hurt1.get()])
        i-=1
    if i>0:
        hurt.extend([hurt2.get()])
        i-=1
    if i>0:
        hurt.extend([hurt3.get()])
        i-=1
    if i>0:
        hurt.extend([hurt4.get()])
        i-=1
    if i>0:
        hurt.extend([hurt5.get()])
        i-=1
    if i>0:
        hurt.extend([hurt6.get()])
        i-=1
    if i>0:
        hurt.extend([hurt7.get()])
        i-=1
    if i>0:
        hurt.extend([hurt8.get()])
        i-=1
    if i>0:
        hurt.extend([hurt9.get()])
        i-=1
    if i>0:
        hurt.extend([hurt10.get()])
        i-=1
    if i>0:
        hurt.extend([hurt11.get()])
        i-=1
    if i>0:
        hurt.extend([hurt12.get()])
        i-=1
    if i>0:
        hurt.extend([hurt13.get()])
        i-=1
    if i>0:
        hurt.extend([hurt14.get()])
        i-=1
    if i>0:
        hurt.extend([hurt15.get()])
        i-=1
    if i>0:
        hurt.extend([hurt16.get()])
        i-=1
    if i>0:
        hurt.extend([hurt17.get()])
        i-=1
    if i>0:
        hurt.extend([hurt18.get()])
        i-=1
    if i>0:
        hurt.extend([hurt19.get()])
        i-=1
    if i>0:
        hurt.extend([hurt20.get()])
        i-=1
    if i>0:
        hurt.extend([hurt21.get()])
        i-=1
    if i>0:
        hurt.extend([hurt22.get()])
        i-=1
    if i>0:
        hurt.extend([hurt23.get()])
        i-=1
    if i>0:
        hurt.extend([hurt24.get()])
        i-=1
    if i>0:
        hurt.extend([hurt25.get()])
        i-=1
    if i>0:
        hurt.extend([hurt26.get()])
        i-=1
    if i>0:
        hurt.extend([hurt27.get()])
        i-=1
    if i>0:
        hurt.extend([hurt28.get()])
        i-=1
    if i>0:
        hurt.extend([hurt29.get()])
        i-=1
    if i>0:
        hurt.extend([hurt.get()])
        i-=1
    if i>0:
        hurt.extend([hurt31.get()])
        i-=1
##    if i>0:
##        hurt.extend([hurt32.get()])
##        i-=1
##    if i>0:
##        hurt.extend([hurt33.get()])
##        i-=1
    #do damage
    global hp
    i=len(final)
    i -=1
    while i>0:
        hp[i]=hp[i]-hurt[i]
        i -=1
    #show new hp
    i=len(final)
    j=(1)
    i -=1
    while i>0:   
        Label(battle, font="time 10", relief=RIDGE,width=5, text = hp[j]).grid(row=j, column=2)
        i -=1
        j +=1
        
    #reset damage
    hurt1.set(0)
    hurt2.set(0)
    hurt3.set(0)
    hurt4.set(0)
    hurt5.set(0)
    hurt6.set(0)
    hurt7.set(0)
    hurt8.set(0)
    hurt9.set(0)
    hurt10.set(0)
    hurt11.set(0)
    hurt12.set(0)
    hurt13.set(0)
    hurt14.set(0)
    hurt15.set(0)
    hurt16.set(0)
    hurt17.set(0)
    hurt18.set(0)
    hurt19.set(0)
    hurt20.set(0)
    hurt21.set(0)
    hurt22.set(0)
    hurt23.set(0)
    hurt24.set(0)
    hurt25.set(0)
    hurt26.set(0)
    hurt27.set(0)
    hurt28.set(0)
    hurt29.set(0)
    hurt30.set(0)
    hurt31.set(0)
    ##hurt32.set(0)
    ##hurt33.set(0)

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
##numlist32=IntVar()
##numlist33=IntVar()

    #Enemy hp
hplist1=IntVar()
hplist2=IntVar()
hplist3=IntVar()
hplist4=IntVar()
hplist5=IntVar()
hplist6=IntVar()
hplist7=IntVar()
hplist8=IntVar()
hplist9=IntVar()
hplist10=IntVar()
hplist11=IntVar()
hplist12=IntVar()
hplist13=IntVar()
hplist14=IntVar()
hplist15=IntVar()
hplist16=IntVar()
hplist17=IntVar()
hplist18=IntVar()
hplist19=IntVar()
hplist20=IntVar()
hplist21=IntVar()
hplist22=IntVar()
hplist23=IntVar()
hplist24=IntVar()
hplist25=IntVar()
hplist26=IntVar()
hplist27=IntVar()
hplist28=IntVar()
hplist29=IntVar()
hplist30=IntVar()
hplist31=IntVar()
##hplist32=IntVar()
##hplist33=IntVar()
hpnew=IntVar()

    #damage done
hurt1=IntVar()
hurt2=IntVar()
hurt3=IntVar()
hurt4=IntVar()
hurt5=IntVar()
hurt6=IntVar()
hurt7=IntVar()
hurt8=IntVar()
hurt9=IntVar()
hurt10=IntVar()
hurt11=IntVar()
hurt12=IntVar()
hurt13=IntVar()
hurt14=IntVar()
hurt15=IntVar()
hurt16=IntVar()
hurt17=IntVar()
hurt18=IntVar()
hurt19=IntVar()
hurt20=IntVar()
hurt21=IntVar()
hurt22=IntVar()
hurt23=IntVar()
hurt24=IntVar()
hurt25=IntVar()
hurt26=IntVar()
hurt27=IntVar()
hurt28=IntVar()
hurt29=IntVar()
hurt30=IntVar()
hurt31=IntVar()
##hurt32=IntVar()
##hurt33=IntVar()

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
Entry(battle,font= "Times 30", width=5,textvariable=newinit).place(relx=.75, rely=.7, anchor="center")
Entry(battle,font= "Times 30", width=5,textvariable=hpnew).place(relx=.85, rely=.7, anchor="center")
    #Name to be Killed
kill_name=Entry(battle,font= "Times 30", width=15)
kill_name.place(relx=.3, rely=.7, anchor="center")
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
##Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist32).grid(row=32, column=1)
##Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=numlist33).grid(row=33, column=1)
    #Enemy HP
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist1).grid(row=1, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist2).grid(row=2, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist3).grid(row=3, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist4).grid(row=4, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist5).grid(row=5, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist6).grid(row=6, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist7).grid(row=7, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist8).grid(row=8, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist9).grid(row=9, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist10).grid(row=10, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist11).grid(row=11, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist12).grid(row=12, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist13).grid(row=13, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist14).grid(row=14, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist15).grid(row=15, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist16).grid(row=16, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist17).grid(row=17, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist18).grid(row=18, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist19).grid(row=19, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist20).grid(row=20, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist21).grid(row=21, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist22).grid(row=22, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist23).grid(row=23, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist24).grid(row=24, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist25).grid(row=25, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist26).grid(row=26, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist27).grid(row=27, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist28).grid(row=28, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist29).grid(row=29, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist30).grid(row=30, column=2)
Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist31).grid(row=31, column=2)
##Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist32).grid(row=32, column=2)
##Entry(init,font= "times 10", relief=RIDGE,width=15,textvariable=hplist33).grid(row=33, column=2)
    #Damage tracker

#Enimy identifier 
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=1, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=2, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=3, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=4, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=5, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=6, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=7, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=8, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=9, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=10, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=11, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=12, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=13, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=14, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=15, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=16, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=17, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=18, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=19, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=20, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=21, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=22, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=23, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=24, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=25, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=26, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=27, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=28, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=29, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=30, column=1)
Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=31, column=1)
##Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=32, column=1)
##Entry(battle,font= "times 10", relief=RIDGE,width=15).grid(row=33, column=1)

#Damage
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt1).grid(row=1, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt2).grid(row=2, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt3).grid(row=3, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt4).grid(row=4, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt5).grid(row=5, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt6).grid(row=6, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt7).grid(row=7, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt8).grid(row=8, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt9).grid(row=9, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt10).grid(row=10, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt11).grid(row=11, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt12).grid(row=12, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt13).grid(row=13, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt14).grid(row=14, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt15).grid(row=15, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt16).grid(row=16, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt17).grid(row=17, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt18).grid(row=18, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt19).grid(row=19, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt20).grid(row=20, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt21).grid(row=21, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt22).grid(row=22, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt23).grid(row=23, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt24).grid(row=24, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt25).grid(row=25, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt26).grid(row=26, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt27).grid(row=27, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt28).grid(row=28, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt29).grid(row=29, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt30).grid(row=30, column=3)
Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt31).grid(row=31, column=3)
##Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt32).grid(row=32, column=3)
##Entry(battle,font= "times 10", relief=RIDGE,width=5,textvariable=hurt33).grid(row=33, column=3)
    


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
Label(battle, bg="grey", font="time 30", text =("New Enemy")).place(relx=.8, rely=.6, anchor="center")
Label(battle, bg="grey", font="time 30", text =("Initiative")).place(relx=.75, rely=.65, anchor="center")
Label(battle, bg="grey", font="time 30", text =("HP")).place(relx=.85, rely=.65, anchor="center")
    #Timer
Label(battle, font="time 60", width=4 ,text = 30).place(relx=.9, rely=.2, anchor="center")
    #Covers
cover=Label(init, bg="grey",width=15, height=50,)
cover.grid(row=1, column=1 , rowspan=40)

cover2=Label(battle, bg="grey",width=13, height=50,)
cover2.grid(row=1, column=1 , rowspan=33)

cover3=Label(battle, bg="grey",width=10, height=50,)
cover3.grid(row=1, column=1 , rowspan=33)

cover4=Label(init, bg="grey",width=15, height=50,)
cover4.grid(row=1, column=1 , rowspan=33)

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
Button(battle, font="times 40",command = lambda:kill(), bg="red", text='Kill').place(relx=.3, rely=.8, anchor="center")
Button(battle, font="times 40",command = lambda:add_enemy(), bg="orange", text='Add Enemy').place(relx=.8, rely=.8, anchor="center")
Button(battle, font="times 30 bold", text = 'Do Damage',command = lambda:dodamage(), bg='red').place(relx=.3, rely=.05, anchor="center")

#Start Gui  
chng_frame(start)

#Main Loop
root.mainloop()


