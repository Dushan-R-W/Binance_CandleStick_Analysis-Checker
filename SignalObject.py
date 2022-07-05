# ------------------
# Function object
# ------------------
class Signal(object):
  def __init__(self, SigName, entryPri, leverage, tp1, tp2, tp3, tp4, stoploss, tradeType, signalDate, signalTime):
    
    self.SigName = SigName
    self.entryPri = entryPri
    self.leverage = leverage
    self.tp1 = tp1
    self.tp2 = tp2
    self.tp3 = tp3
    self.tp4 = tp4
    self.stoploss = stoploss
    self.tradeType = tradeType
    self.signalDate = signalDate
    self.signalTime = signalTime
  
