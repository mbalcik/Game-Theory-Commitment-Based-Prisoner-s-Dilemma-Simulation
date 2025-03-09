class GrimTrigger():
     
     def play(self, botHistory, botBudget, roundNum):
          #print("Grim Trigger")
          if ('D' in botHistory) :
               return False
          else :
               return True
          

     def name(self):
        return "grimtrigger"

     def stratInt(self):
        return 5