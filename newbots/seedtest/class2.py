import random 

class Class2:
    def __init__(self, class1, seed):
        self.class1 = class1
        self.seed = seed 
        random.seed(self.seed)



    def seedList2(self):
        print("class2's list: ")
        for i in range(10): 
            if i != 9 : print(random.randrange(1,101), end=" ")
            else : print(random.randrange(1,101))
    