class GenerousTitForTat():
    def __init__(self):
        self.revenge = False

    def setRevenge(self, flag):
        self.revenge = flag

    def getRevenge(self):
        return self.revenge
    
    def play(self, botHistory, botBudget, roundNum):
        #print("Generous tit for tat")
        if botHistory == []:
            self.setRevenge(False)

        if botHistory == [] or len(botHistory) < 4:
            return True
        else:
            if self.getRevenge():
                self.setRevenge(False)
                return False
            elif (botHistory[2*roundNum-1] == "D" and botHistory[2*roundNum-3] == "D"):
                self.setRevenge(True)
                return False
            else:
                return True
            
    def name(self):
        return "generoustitfortat"
    
    def stratInt(self):
        return 3