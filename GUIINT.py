from tkinter import *
from pros import *
# graphical interface class
class GUI:
    def __init__(self,m,frame,Q1,Q2,Q3,Q4,lsc,lsio,lspri,b,b2,b3):
        self.m = m
        self.frame = frame
        self.Q1 = Q1
        self.Q2 = Q2
        self.Q3 = Q3
        self.Q4 = Q4
        self.lsc = lsc
        self.lsio = lsio
        self.lspri = lspri
        self.b = b
        self.b2 = b2
        self.b3 = b3






# start window
    def FirShow(self,e1,e2):
        p = 5
        l1 = Label(self.frame, width=50,fg="blue",background="snow",justify=CENTER,text="Welcome to my project, which is: ")
        l1.grid(row=0, column=0, padx=p, pady=p)
        l2 = Label(self.frame, width=50,fg="blue",background="snow",justify=CENTER,text="Simulating Multilevel Feedback Queue Scheduling.")
        l2.grid(row=1, column=0, padx=p, pady=p)
        l3 = Label(self.frame, width=50,fg="blue",background="snow",justify=CENTER,text="Enter Sleep Time: ")
        l3.grid(row=2, column=0, padx=p, pady=p)
        e1.grid(row=2, column=1, padx=p, pady=p)
        l4 = Label(self.frame, width=50, fg="blue", background="snow", justify=CENTER, text="Enter Alpha: ")
        l4.grid(row=3, column=0, padx=p, pady=p)
        e2.grid(row=3, column=1, padx=p, pady=p)
        self.b3.grid(row=4, column=0, padx=p, pady=p)



# runtime window
    def Show(self,z):
        w = 9
        p = 5
        if(len(self.lsc) >13):
            w = 5
            p = 3
        self.e = Entry(self.frame, width=w, fg="blue",background="snow",justify=CENTER)
        self.e.grid(row=0, column=0,padx=p,pady=p)
        self.e.insert(END,"Que 1")
        i = 0
        while(i<len(self.Q1)):
            self.e = Entry(self.frame,width=w,fg="blue",background="snow",justify=CENTER)
            self.e.grid(row=0,column=i+1,padx=p,pady=p)
            self.e.insert(END,self.Q1[i].pid)
            i += 1


        self.e = Entry(self.frame, width=w,fg="blue",background="snow",justify=CENTER)
        self.e.grid(row=1, column=0,padx=p,pady=p)
        self.e.insert(END, "Que 2")
        i = 0
        while (i < len(self.Q2)):
            self.e = Entry(self.frame, width=w,fg="blue",background="snow",justify=CENTER)
            self.e.grid(row=1, column=i+1,padx=p,pady=p)
            self.e.insert(END, self.Q2[i].pid)
            i += 1



        self.e = Entry(self.frame, width=w, fg="blue",background="snow",justify=CENTER)
        self.e.grid(row=2, column=0,padx=p,pady=p)
        self.e.insert(END, "Que 3")
        i = 0
        while (i < len(self.Q3)):
            self.e = Entry(self.frame, width=w, fg="blue",background="snow",justify=CENTER)
            self.e.grid(row=2, column=i+1,padx=p,pady=p)
            self.e.insert(END, self.Q3[i].pid)
            i += 1



        self.e = Entry(self.frame, width=w, fg="blue",background="snow",justify=CENTER)
        self.e.grid(row=3, column=0,padx=p,pady=p)
        self.e.insert(END, "Que 4")
        i = 0
        while (i < len(self.Q4)):
            self.e = Entry(self.frame, width=w, fg="blue",background="snow",justify=CENTER)
            self.e.grid(row=3, column=i+1,padx=p,pady=p)
            self.e.insert(END, self.Q4[i].pid)
            i += 1





        self.e = Entry(self.frame, width=w, fg="black",background="red",justify=CENTER)
        self.e.grid(row=4, column=0,padx=p,pady=p)
        self.e.insert(END, "CPU")
        i = 0
        while (i < len(self.lsc)):
            if(self.lsc[i].emp == True):
                self.e = Entry(self.frame, width=w, fg="black",background="red",justify=CENTER)
                self.e.grid(row=4, column=i+1,padx=p,pady=p)
                self.e.insert(END, self.lsc[i].pi)
                break
            i += 1

        self.e = Entry(self.frame, width=w, fg="red",background="gold",justify=CENTER)
        self.e.grid(row=5, column=0,padx=p,pady=p)
        self.e.insert(END, "IO")
        i = 0
        while (i < len(self.lsio)):
            if (self.lsio[i].emp == True):
                self.e = Entry(self.frame, width=w, fg="red",background="gold",justify=CENTER)
                self.e.grid(row=5, column=i+1,padx=p,pady=p)
                self.e.insert(END, self.lsio[i].pi)
            i += 1

        self.e = Entry(self.frame, width=w+4, fg="dark green",background="cyan",justify=CENTER)
        self.e.grid(row=6, column=0,padx=p,pady=p)
        self.e.insert(END, "Prediction")
        i = 0
        while (i < len(self.lspri)):
            self.e = Entry(self.frame, width=w+4, fg="dark green",background="cyan",justify=CENTER)
            self.e.grid(row=6, column=i + 1,padx=p,pady=p)
            self.e.insert(END, (str(self.lspri[i].pid)+">>"+str(self.lspri[i].pre)))
            i += 1
        L = Label(self.frame,width=15,fg="red",justify=CENTER,text="counter: "+ str(z))
        L.grid(row=7,column=0,pady=p,padx=p)
        self.b.grid(row=7,column=2,padx=p,pady=p)
        self.b2.grid(row=7, column=1, padx=p, pady=p)





# results window
    def Show2(self,G1,G2,Avg,Utlaiz):
        self.l = Label(self.frame,width=15,background="snow",fg="blue",text="AvgWaiting: ",justify=CENTER)
        self.l.grid(row=0,column=0,pady=10)
        self.l2 = Label(self.frame,width=15,background="snow",fg="blue",text=str(Avg),justify=CENTER)
        self.l2.grid(row=0, column=1,pady=10,padx=3)
        self.l = Label(self.frame,width=15,background="snow",fg="blue",text="CPU utilization: ",justify=CENTER)
        self.l.grid(row=0,column=2,pady=10)
        self.l2 = Label(self.frame,width=15,background="snow",fg="blue",text=str(Utlaiz),justify=CENTER)
        self.l2.grid(row=0, column=3,pady=10,padx=3)

        self.e = Entry(self.frame, width=20, fg="red",background="gold",justify=CENTER)
        self.e.grid(row=2, column=0,pady=10)
        self.e.insert(END, "GACPU: pid->time")
        w = 13
        i = 0
        ro = len(G1)//7
        if (ro < 2):
            ro += 1
        n = 2
        k = 0
        while (i < len(G1)):
            if(k == ro):
                n += 1
                k = 0
            self.e = Entry(self.frame, width=w, fg="red",background="gold",justify=CENTER)
            self.e.grid(row=n, column=k+1,pady=5,padx=4)
            self.e.insert(END,str(G1[i].pid) + "->" + str(G1[i].gan))
            i += 1
            k += 1

        self.e = Entry(self.frame, width=20, fg="dark green",background="cyan",justify=CENTER)
        self.e.grid(row=n+1, column=0, pady=10)
        self.e.insert(END, "GAIO: pids->time")
        i = 0
        ro = len(G2) // 7
        if(ro<2):
            ro += 1
        n = n +1
        k = 0
        while (i < len(G2)):
            if (k == ro):
                n += 1
                k = 0
            self.e = Entry(self.frame, width=w, fg="dark green",background="cyan",justify=CENTER)
            self.e.grid(row=n, column=k+1,pady=5,padx=4)
            self.e.insert(END, G2[i].pids + "->" + str(G2[i].gan))
            i += 1
            k += 1



