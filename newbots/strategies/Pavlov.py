class Pavlov():

    def play(self, botHistory, botBudget, roundNum):
        #print("Pavlov")
        if botHistory == []:
            return True
        if (botHistory[2*roundNum-2] == "C") and (botHistory[2*roundNum-1]=="D"):
            return False
        return True
    
    def name(self):
        return "pavlov"
    
    def stratInt(self):
        return 1