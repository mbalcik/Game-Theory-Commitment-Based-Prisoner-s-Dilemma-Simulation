class TitForTat():

    def play(self, botHistory, botBudget, roundNum) :
        #print("Titfortat")
        if botHistory == []:
            return True #True for cooperation
        else:
            if (botHistory[2*roundNum-1] == "C") : 
                return True
            else :
                return False #False for defection
            
    def name(self):
        return "titfortat"
    
    def stratInt(self):
        return 4