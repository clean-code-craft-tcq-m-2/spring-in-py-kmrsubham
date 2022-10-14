import math



class EmailAlert:
    def __init__(self, emailSent=True):
        self.emailSent = emailSent



   def alert():
        self.emailSent = True




class LEDAlert:
    def __init__(self, ledGlows=True):
        self.ledGlows = ledGlows



   def alert():
        self.ledGlows = True



class StatsAlerter:
    def __init__(self, v1, v2):
        self.maxThreshold = v1
        self.list = v2



   def checkAndAlert(self, v):
        val = max(v)
        if val > self.maxThreshold:
            self.list[0].emailSent = True
            self.list[1].ledGlows = True
            
            
def calculateStats(numbers):
  computedStats = {}
  if len(numbers) == 0:
    computedStats["avg"] = math.nan
    computedStats["max"] = math.nan
    computedStats["min"] = math.nan
  else:
    computedStats["avg"] = sum(numbers)/len(numbers)
    computedStats["max"] = max(numbers)
    computedStats["min"] = min(numbers)
  return computedStats
