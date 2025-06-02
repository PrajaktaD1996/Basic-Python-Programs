#file-1
from threading import*

class Test(Thread):
    #def fun(self,num):
        #self.newnum = num*4
        #print("fun call:"+str(self.newnum))

    ##calculate
    def __init__(self,name,a,b):
        Thread.__init__(self)
        #variables are accessed
        self.name = name 
        self.summ = a+b
        self.subb = a-b
        self.val  = 90 
        self.fun(5)
   
    ##print here
    def run(self):
        for i in range(2):
            print(self.name)
        print(self.summ)
        print(self.subb)

    def sam(self):
        return self.val

    def fun(self,num):
        self.newnum = num*4
        print("fun call:"+str(self.newnum))

    
#test object
obj1 = Test("hello",9,4)
