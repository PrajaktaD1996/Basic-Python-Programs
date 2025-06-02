import file1 as f1obj
import file2 as f2obj
from threading import*


f1obj.Test("hello",9,4).run()
#f2obj.Test("world",10,2).run() ###thread with parameters
#f2obj.Test().run()  ###thread without parameters it will print the parameters

#var2 = f2obj.Test("world",9,3).sam() #thread with parameters
var2 = f2obj.Test().sam()             #thread without parameters

var1 = f1obj.Test("gvjh",8,5).sam()

print("valfile1:"+str(var1)+" valfile2:"+str(var2))


####
#f1_obj = f1.c1()

#th1_c1_obj1 = Thread(target=f1_obj.fun1())
#th1_c1_obj2 = Thread(target=f1_obj.fun2())

#th1_c1_obj1.start()
#th1_c1_obj2.start()

#th1_c1_obj1.join()
#th1_c1_obj2.join()

#####


#obj = f1.Test()

