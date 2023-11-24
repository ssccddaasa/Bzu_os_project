#Saleh Khatib 1200991
#Project: Simulating Multilevel Feedback Queue Scheduling
#GUIINT is graphical interface class
from GUIINT import *
import time
#prosesses file with there all information
f = open("Workload.txt","r")
lsPros = []
qr = []
for x in f:
    qr.append(x)
for x in qr:
    x = x.replace("\n","")
    x = x.replace("\t"," ")
    s = x.split(" ")
    print(s)
    lsint = []
    for y in s:
        lsint.append(int(y))
    p = pro(lsint[0],lsint[1],lsint[2:])
    lsPros.append(p)


# check if process arrived or not
def IsArr(i,p):
    if(i == p.arri):
        return True
    else:
        return False
# check if process finish or not
def OnePcheck(p):
    sum = 0
    for x in p.lsCIO:
        sum += x
    if (sum == 0):
        return True
    else:
        return False
# check all processes if thay are finish or not
def AllPcheck(ls):
    for x in ls:
        if(OnePcheck(x) == False):
            return False
    return True
# returns the current CPU brust
def WhereAmICPU(p):
    i = 0
    while(i<len(p.lsCIO)):
        if(p.lsCIO[i]>0):
            return i
        i += 2
    return 9999
# returns the current IO brust
def WhereAmInIO(p):
    if(len(p.lsCIO)<2):
        return 9999
    else:
        i = 1
        while(i<len(p.lsCIO) - 1):
            if(p.lsCIO[i]>0):
                return i
            i += 2
        return 9999
# returns where is the process in Que
def WhereInQue(Q,pid):
    for x in range(len(Q)):
        if(Q[x].pid == pid):
            return x
    return -15

# Ques,CPU,and IO
Que1 = []
Que2 = []
Que3 = []
Que4 = []

lsCPU = []
lsIO = []
for x in lsPros:
    temp = CPU(x.pid,"1",False,0-x.arri)
    lsCPU.append(temp)
for x in lsPros:
    temp2 = CPU(x.pid,"1",False,0)
    lsIO.append(temp2)
SHh3 = []
for x in lsPros:
    temmp = SCHH3(x.pid,9999.0,0)
    SHh3.append(temmp)

# check if CPU is running or not
def CPUcheck(ls):
    for x in ls:
        if(x.emp == True):
            return True
    return False

# returns the process on CPU
def FindP(lsc):
    for x in lsc:
        if(x.emp == True):
             return x.pi
    return 9

# move process form Que to other
def Move1(Q1,Q2,i):
    x = Q1.pop(i)
    Q2.append(x)


couq1: int = 0
couq2: int = 0
# add the process to Que1 based on arrivel time
def AddArri(Q1,lsp,i):
    x = 0
    while(x<len(lsp)):
        if(IsArr(i,lsp[x]) == True):
            pte = lsp.pop(x)
            Q1.append(pte)
            x -= 1
        x += 1


# scheduling Que1 according to the conditions given in the explanation
def Sch1(Q1, Q2, lsc, lsio,lspri):
    global couq1
    if(CPUcheck(lsc) == True):
        fou = FindP(lsc)
        if(lsc[fou].q != "1"):
            if (lsc[fou].q == "3"):
                for z in Q1:
                    if (lsio[z.pid].emp == False):
                        lsc[fou].SetFalse()
                        for u in range(len(lspri)):
                            if (lspri[u].pid == lsc[fou].pi):
                                lspri[u].PlusRpe()
                                break
                        lsc[z.pid].SetTrue()
                        return 0
            else:
                for z in Q1:
                    if (lsio[z.pid].emp == False):
                        lsc[fou].SetFalse()
                        lsc[z.pid].SetTrue()
                        return 0
            return 0
        else:
            if(couq1 >= 10):
                lsc[fou].SetFalse()
                lsc[fou].SetQue("2")
                lsio[fou].SetQue("2")
                u = WhereInQue(Q1,lsc[fou].pi)
                Move1(Q1,Q2,u)
                couq1 = 0
                if(len(Q1)>0):
                    i = 0
                    new = Q1[0].pid
                    while (i < len(Q1)):
                        new = Q1[i].pid
                        if (lsio[new].emp == False):
                            lsc[new].SetTrue()
                            lsc[new].SetQue("1")
                            return 0
                        i += 1
                    return 0
                else:
                    return 0
            else:
                couq1 += 1
                return 0
    else:
        couq1 = 0
        i = 0
        new = Q1[0].pid
        while (i < len(Q1)):
            new = Q1[i].pid
            print(new)
            if (lsio[new].emp == False):
                lsc[new].SetTrue()
                lsc[new].SetQue("1")
                return 0
            i += 1
        return 0



def findpri(lspri,pId):
    for x in range(len(lspri)):
        if(lspri[x].pid == pId):
            return x





# scheduling Que2 according to the conditions given in the explanation
def Sch2(Q1, Q2, lsc, lsio,lspri):
    ou = 0
    global couq2
    if(CPUcheck(lsc) == True):
        fou = FindP(lsc)
        if(lsc[fou].q != "2"):
            if(lsc[fou].q == "3"):
                for z in Q1:
                    if (lsio[z.pid].emp == False):
                        lsc[fou].SetFalse()
                        for u in range(len(lspri)):
                            if(lspri[u].pid == lsc[fou].pi):
                                lspri[u].PlusRpe()
                                break
                        lsc[z.pid].SetTrue()
                        return 0
            elif(lsc[fou].q == "4"):
                for z in Q1:
                    if (lsio[z.pid].emp == False):
                        lsc[fou].SetFalse()
                        lsc[z.pid].SetTrue()
                        return 0

            return 0
        else:
            if(couq2 >= 9):
                lsc[fou].SetFalse()
                lsc[fou].SetQue("3")
                lsio[fou].SetQue("3")
                u = WhereInQue(Q1,lsc[fou].pi)
                ou = findpri(lspri,Q1[u].pid)
                lspri[ou].pre = 8
                Move1(Q1,Q2,u)
                couq2 = 0
                if(len(Q1)>0):
                    i= 0
                    new = Q1[0].pid
                    while (i < len(Q1)):
                        new = Q1[i].pid
                        if (lsio[new].emp == False):
                            lsc[new].SetTrue()
                            lsc[new].SetQue("2")
                            return 0
                        i += 1
                    return 0
                else:
                    return 0
            else:
                couq2 += 1
                return 0
    else:
        couq2 = 0
        i = 0
        new = Q1[0].pid
        while(i<len(Q1)):
            new = Q1[i].pid
            if(lsio[new].emp == False):
                lsc[new].SetTrue()
                lsc[new].SetQue("2")
                return 0
            i += 1
        return 0

def getpp(p):
    return p.getpre()
def Sorot(ls):
    ls.sort(key=getpp)

def New(Q,lspri,lsio,pidd):
    for x in lspri:
        new = WhereInQue(Q,x.pid)
        if(new == -15):
            continue
        if(lsio[Q[new].pid].emp == False):
            if(new == pidd):
                return -19
            return Q[new].pid
        else:
            continue
    return -15

# scheduling Que3 according to the conditions given in the explanation

def Sch3(Q1, Q2, lsc, lsio,lspri):
    ou = 0
    if(CPUcheck(lsc) == True):
        fou = FindP(lsc)
        if (lsc[fou].q != "3"):
            if(lsc[fou].q == "4"):
                for z in Q1:
                    if (lsio[z.pid].emp == False):
                        lsc[fou].SetFalse()
                        lsc[z.pid].SetTrue()
                        return 0
            return 0
        else:
            Sorot(lspri)
            if(lsc[fou].pi != lspri[0].pid):
                uy = WhereInQue(Q1,lsc[fou].pi)
                lsc[fou].SetFalse()
                ou = findpri(lspri,lsc[fou].pi)
                new = New(Q1,lspri,lsio,uy)
                if(new == -15):
                    return -9
                if(new == -19):
                    new = fou
                    lspri[ou].rpe -= 1
                lsc[new].SetTrue()
                lspri[ou].PlusRpe()
            if(lspri[ou].rpe>=3):
                lsc[fou].SetFalse()
                lsc[fou].SetQue("4")
                lsio[fou].SetQue("4")
                u = WhereInQue(Q1, lsc[fou].pi)
                Move1(Q1, Q2, u)
                lspri.pop(ou)
                if (len(Q1) > 0):
                    i = 1
                    new = lspri[0].pid
                    while (i < len(lspri)):
                        new = lspri[i].pid
                        if (lsio[new].emp == False):
                            lsc[new].SetTrue()
                            lsc[new].SetQue("3")
                            return 0
                        i += 1
                    return 0
                else:
                    return 0
    else:
        Sorot(lspri)
        i = 0
        new = lspri[0].pid
        while (i < len(lspri)):
            new = lspri[i].pid
            if (lsio[new].emp == False):
                lsc[new].SetTrue()
                lsc[new].SetQue("3")
                return 0
            i += 1
        return 0



# scheduling Que4 according to the conditions given in the explanation
def Sch4(Q1, lsc, lsio):
    if (CPUcheck(lsc) == True):
        fou = FindP(lsc)
        if (lsc[fou].q != "4"):
            return 0
    else:
        i = 0
        new = Q1[0].pid
        while (i < len(Q1)):
            new = Q1[i].pid
            if (lsio[new].emp == False):
                lsc[new].SetTrue()
                lsc[new].SetQue("4")
                return 0
            i += 1
        return 0

# functions for Manage IO and Ques
def ManHel(p,wh,x):
    p.lsCIO[wh] -= 1
    if(p.lsCIO[wh] == 0):
        x.SetFalse()
def ManHel24(Q,wh,x,i):
    Q[i].lsCIO[wh] -= 1
    if(Q[i].lsCIO[wh] == 0):
        x.SetFalse()
        c = Q.pop(i)
        Q.append(c)

def IOMang(lsio,Q1,Q2,Q3,Q4):
    for x in lsio:
        if(x.emp == True):
            if(x.q == "1"):
               wh = WhereInQue(Q1,x.pi)
               whbr = WhereAmInIO(Q1[wh])
               ManHel(Q1[wh],whbr,x)
            elif (x.q == "2"):
                wh = WhereInQue(Q2,x.pi)
                whbr = WhereAmInIO(Q2[wh])
                ManHel(Q2[wh], whbr, x)
            elif (x.q == "3"):
                wh = WhereInQue(Q3,x.pi)
                whbr = WhereAmInIO(Q3[wh])
                ManHel(Q3[wh], whbr, x)
            elif (x.q == "4"):
                wh = WhereInQue(Q4,x.pi)
                whbr = WhereAmInIO(Q4[wh])
                ManHel24(Q4, whbr, x,wh)


# functions for Manage CPU and Ques
lsFin = []
def Manhel2(p,wh,x,lsio,Q,whq,lspri):
    ou = 0
    p.lsCIO[wh] -= 1
    if(OnePcheck(p) == True):
        ou = findpri(lspri,p.pid)
        lspri.pop(ou)
        fin = Q.pop(whq)
        lsFin.append(fin)
        x.SetFalse()
    else:
        if (p.lsCIO[wh] == 0):
            x.SetFalse()
            lsio[x.pi].SetTrue()
def Manhel2S4(p,wh,x,lsio,Q,whq):
    p.lsCIO[wh] -= 1
    if(OnePcheck(p) == True):
        fin = Q.pop(whq)
        lsFin.append(fin)
        x.SetFalse()
    else:
        if (p.lsCIO[wh] == 0):
            x.SetFalse()
            lsio[x.pi].SetTrue()

lsPrid = []
lsActul = []
for x in range(len(lsPros)):
    lsPrid.append(0)
    lsActul.append(0)


# calling the graphical interface class and make the start window

def Focus(ev,e):
    e.delete(0, END)

# exit the statr window
def LetsGo(e1,e2):
    global m1
    global Alpha
    global sleep
    sleep = e1.get()
    Alpha = e2.get()
    if(sleep.isnumeric() == False or sleep == ""):
        sleep = "0.0"
    if(Alpha.isnumeric() == False or Alpha == ""):
        Alpha = "0.5"
    m1.destroy()

m1 = Tk()
m1.geometry("1200x600")
m1.config(bg="gray13")
Fre1 = Frame(m1)
Fre1.config(bg="gray13")
b = Button(Fre1, width=10, text="stop", fg="red")
b2 = Button(Fre1, width=10, text="start", fg="red")
b3 = Button(Fre1, width=10, text="Start", fg="red", command=lambda:LetsGo(e1,e2))
e1 = Entry(Fre1, width=40,fg="blue",background="green",justify=CENTER)
e1.insert(END, "1 = 100ms Def = 0")
e1.bind("<Button-1>", lambda event: Focus(event, e1))
e2 = Entry(Fre1, width=40, fg="blue", background="green", justify=CENTER)
e2.insert(END, "1 = 0.1 Def = 0.5")
e2.bind("<Button-1>", lambda event: Focus(event, e2))

Alpha = ""
sleep = ""

g = GUI(m1,Fre1,Que1,Que2,Que3,Que4,lsCPU,lsIO,SHh3,b,b2,b3)
slal = g.FirShow(e1,e2)
Fre1.place(relx=.5, rely=.5, anchor=CENTER)
m1.mainloop()










# the eqution function for Que3(SRTF) to calculate predicted CPU brust
def eqution(lspri,lsPr,lsAu,i,j):
    global Alpha
    alpha = float(Alpha)/10
    e1 = alpha*lsAu[i]
    e2 = (1-alpha)*lsPr[i]
    lspri[j].pre = e2 + e1
    lsPr[i] = 0
    lsAu[i] = 0
# functions for Manage CPU and Ques (ManHelS3 for Que3)
def ManHelS3(p,wh,x,lsio,Q,whq,lsPr,lsAu,lspri):
    ou = findpri(lspri,p.pid)
    lsPr[p.pid] += 1
    lsAu[p.pid] += 1
    lspri[ou].pre -= 1
    p.lsCIO[wh] -= 1
    if(OnePcheck(p) == True):
        fin = Q.pop(whq)
        lspri.pop(ou)
        lsFin.append(fin)
        x.SetFalse()
    else:
        if (p.lsCIO[wh] == 0):
            lsPr[p.pid] += lspri[ou].pre
            eqution(lspri,lsPr,lsAu,p.pid,ou)
            x.SetFalse()
            lsio[x.pi].SetTrue()

def CPUMang(lsc,lsio,Q1,Q2,Q3,Q4,lspri,lsPr,lsAu):
    for x in lsc:
        if(x.emp == True):
            if(x.q == "1"):
               wh = WhereInQue(Q1,x.pi)
               whbr = WhereAmICPU(Q1[wh])
               Manhel2(Q1[wh],whbr,x,lsio,Q1,wh,lspri)
            elif (x.q == "2"):
                wh = WhereInQue(Q2,x.pi)
                whbr = WhereAmICPU(Q2[wh])
                Manhel2(Q2[wh], whbr, x, lsio, Q2, wh,lspri)
            elif (x.q == "3"):
                wh = WhereInQue(Q3,x.pi)
                whbr = WhereAmICPU(Q3[wh])
                ManHelS3(Q3[wh], whbr, x, lsio, Q3, wh,lsPr,lsAu,lspri)
            elif (x.q == "4"):
                wh = WhereInQue(Q4,x.pi)
                whbr = WhereAmICPU(Q4[wh])
                Manhel2S4(Q4[wh], whbr, x, lsio, Q4, wh)
            break




# function to to calculate the waitting time for evrey process
def Wating(lsc,lsio,fin):
    lswt = []
    for i in range(len(lsc)):
        if(lsc[i].emp == True or lsio[i].emp == True):
            lswt.append(i)
    if(len(fin)>0):
        for i in range(len(fin)):
            lswt.append(fin[i].pid)
    lswf = []
    for x in lsc:
        if(x.pi in lswt):
            pass
        else:
            lswf.append(x.pi)
    for k in lswf:
        lsc[k].wait += 1







GannarCPU = []
GannarIO = []
# function to make gantt chart for CPU
def Ganner1(lsc,G1,i):
    for x in lsc:
        if(x.emp == True):
            if(len(G1) == 0):
                t1 = GCPU(x.pi,i)
                G1.append(t1)
            else:
                if(G1[-1].pid == x.pi):
                    G1[-1].gan += 1
                else:
                    t1 = GCPU(x.pi, i)
                    G1.append(t1)


# function to make gantt chart for IO
def Ganner2(lsio,G2,i):
    s = ""
    for x in lsio:
        if(x.emp == True):
          s = s + str(x.pi)

    if(s != ""):
        if(len(G2) == 0):
            t2 = GIO(s,i)
            G2.append(t2)
        else:
            if(G2[-1].pids == s):
                G2[-1].gan += 1
            else:
                t2 = GIO(s, i)
                G2.append(t2)




# make runtime window
sss = 1
def Stop():
   global sss
   sss = 0
def Start():
   global sss
   sss = 1

m = Tk()
m.geometry("1200x600")
m.config(bg="gray13")
Fre = Frame(m)
Fre.config(bg="gray13")
b = Button(Fre, width=10, text="Stop", fg="red", command=lambda:Stop())
b2 = Button(Fre, width=10, text="Resume", fg="red", command=lambda:Start())
b3 = Button(Fre, width=10, text="Start", fg="red", command=lambda:LetsGo())









# loop to Simulate scheduling Where the one iteration represents one unit of time
# call all functions to manege the scheduling.
def Pri(Q):
    for x in Q:
        print(x.toStr(),end=" / ")
def Pri2(Q):
    for x in Q:
        print(x.toStr(),end=" / ")
    print("\n")

n = 0
CpuU = 0
slep = float(sleep) / 10
while(len(lsFin)<len(lsCPU)):
    if(len(lsPros)>0):
        AddArri(Que1,lsPros,n)
    if(len(Que1)>0 or CPUcheck(lsCPU) == True):
        Sch1(Que1,Que2,lsCPU,lsIO,SHh3)
    if(len(Que2)>0 or CPUcheck(lsCPU) == True):
        Sch2(Que2,Que3,lsCPU,lsIO,SHh3)
    if(len(Que3)>0 or CPUcheck(lsCPU) == True):
        Sch3(Que3,Que4,lsCPU,lsIO,SHh3)
    if(len(Que4)>0 or CPUcheck(lsCPU) == True):
        Sch4(Que4,lsCPU,lsIO)
    IOMang(lsIO,Que1,Que2,Que3,Que4)
    CPUMang(lsCPU,lsIO,Que1,Que2,Que3,Que4,SHh3,lsPrid,lsActul)
    Wating(lsCPU,lsIO,lsFin)
    Ganner1(lsCPU,GannarCPU,n)
    Ganner2(lsIO,GannarIO,n)
    if(CPUcheck(lsCPU) == True):
        CpuU += 1
    Pri(Que1)
    print("\n1_______________________________________________")
    Pri(Que2)
    print("\n2_______________________________________________")
    Pri(Que3)
    print("\n3_______________________________________________")
    Pri(Que4)
    print("\n4_______________________________________________")
    Pri2(lsCPU)
    Pri2(lsIO)
    for iyu in SHh3:
        print(iyu.Tostr())
    for widget in Fre.winfo_children():
        if(widget.widgetName == "button"):
            continue
        widget.destroy()
    n += 1
    g = GUI(m,Fre,Que1,Que2,Que3,Que4,lsCPU,lsIO,SHh3,b,b2,b3)
    g.Show(n)
    Fre.place(relx=.5, rely=.5, anchor=CENTER)
    time.sleep(slep)
    m.update()
    if(sss == 0):
        while(sss == 0):
            m.update()





# make final window to show the results of the scheduling

Utaliz = CpuU / n
for x in lsCPU:
    print(str(x.pi) + "  " + str(x.wait))
summ = 0
for x in lsCPU:
    summ += x.wait
avg = summ/len(lsCPU)


for x in GannarCPU:
    print(str(x.pid) + "-" + str(x.gan),end="//")
print("\n")
for x in GannarIO:
    print(x.pids + "-" + str(x.gan),end="//")
print("\n")

for widget in Fre.winfo_children():
    widget.destroy()
g = GUI(m,Fre,Que1,Que2,Que3,Que4,lsCPU,lsIO,SHh3,b,b2,b3)
g.Show2(GannarCPU,GannarIO,avg,Utaliz)
Fre.place(relx=.5, rely=.5, anchor=CENTER)


m.mainloop()