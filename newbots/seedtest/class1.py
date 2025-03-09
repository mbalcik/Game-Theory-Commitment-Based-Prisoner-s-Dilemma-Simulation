import random
from datetime import datetime

class Class1():
    def __init__(self):
        self.seed = datetime.now().timestamp()

    def getSeed(self):
        return self.seed

    def seedList1(self):
        random.seed(self.seed)
        print("class1's list: ")
        for i in range(10): 
            if i != 9 : print(random.randrange(1,101), end=" ")
            else : print(random.randrange(1,101))
        