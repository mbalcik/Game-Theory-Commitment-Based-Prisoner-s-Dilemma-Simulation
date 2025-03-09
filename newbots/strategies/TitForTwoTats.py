class TitForTwoTats():
    def play(self, botHistory, botBudget, roundNum):
        #print("titfortwotats")
        if botHistory == [] or len(botHistory) < 4:
            return True
        else:
            if (botHistory[2*roundNum-1] == "D" and botHistory[2*roundNum-3] == "D") : return False
            else :  return True
            
    def name(self):
        return "titfortwotats"
    
    def stratInt(self):
        return 2