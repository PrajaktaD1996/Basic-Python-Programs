#file-2
from threading import*


class Test(Thread):
    def __init__(self):

    ##calculate
    #def __init__(self,name,a,b):
        Thread.__init__(self)
        a=2
        b=4
        name = "hello"
        self.name = name
        self.mul = a*b
        self.div = a/b
        self.val = 50

    ##print here
    def run(self):
        for i in range(2):
            print(self.name)
        print(self.mul)
        print(self.div)

    def sam(self):
        #self.val = 50
        return self.val


#test object
#obj2 = Test("hello",9,4)







