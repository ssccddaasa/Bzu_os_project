# class for processes
class pro:
    def __init__(self,pid,arri,lsCIO):
        self.pid = pid
        self.arri = arri
        self.lsCIO = lsCIO
    def lstostr(self):
        s = ""
        for x in self.lsCIO:
            s = s + " " + str(x)
        return s
    def toStr(self):
        return str(self.pid) + " " + str(self.arri) + self.lstostr()

#class for CPU and IO
class CPU:
    def __init__(self,pi,q,emp,wait):
        self.pi = pi
        self.q = q
        self.emp = emp
        self.wait = wait

    def SetTrue(self):
        self.emp = True
    def SetFalse(self):
        self.emp = False
    def SetQue(self,Q):
        self.q = Q
    def toStr(self):
        return str(self.pi) + " " + self.q + " " + str(self.emp) + " " + str(self.wait)
# class for (SRTF) processes
class SCHH3:
    def __init__(self,pid,pre,rpe):
        self.pid = pid
        self.pre = pre
        self.rpe = rpe

    def mins(self):
        self.pre -= 1
    def getpre(self):
        return float(self.pre)
    def PlusRpe(self):
        self.rpe += 1
    def Tostr(self):
        return str(self.pid) + " / " + str(self.pre) + " / " + str(self.rpe)


# classes for gantt chart for CPU and IO
class GCPU:
    def __init__(self,pid,gan):
        self.pid = pid
        self.gan = gan
class GIO:
    def __init__(self,pids,gan):
        self.pids = pids
        self.gan = gan