from class1 import Class1
from class2 import Class2

class1obj = Class1()

class2obj = Class2(class1obj, class1obj.getSeed())

class1obj.seedList1()
class2obj.seedList2()

