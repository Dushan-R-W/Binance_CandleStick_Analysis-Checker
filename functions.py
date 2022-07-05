from genericpath import isfile
from colorama.ansi import Fore, Style
from numpy.lib.npyio import load
import config
import csv
from binance.client import Client
from numpy import genfromtxt
import os
from datetime import date, datetime, time, timedelta
import pickle
import os
import fnmatch
import SignalObject

postedSignalList = []

# ------------------
# Function delete Files
# ------------------
def deleteFiles(remove_Name):
  if(os.path.exists(remove_Name) and os.path.isfile(remove_Name)):
    os.remove(remove_Name)
    #print(remove_Name + " deleted")
  else:
    #print(remove_Name + " not found")
    print("")


# ------------------
# Function create files
# ------------------
def createFiles(filename):
    open(filename, 'a').close()
    #print(filename + " created empty")


# ------------------
# Function get candle data
# ------------------
def getCandleData(Coinname, fileName,startDate, endDate):
  client = Client(config.API_KEY, config.API_SECRET)
  #print(Fore.WHITE + "Getting candle data"  + Style.RESET_ALL)
  candles = client.get_historical_klines(Coinname, Client.KLINE_INTERVAL_5MINUTE, startDate, endDate)
  csvfile = open(fileName, 'w', newline='')
  candestick_writer = csv.writer(csvfile, delimiter=',')

  for candlestick in candles:
      # print(candlestick)
      candestick_writer.writerow(candlestick)
  #print(Fore.WHITE + "Candle Data saved to " + fileName  + Style.RESET_ALL)


# ------------------
# Function get Individual data
# ------------------
def getIndividualData(column, fileName, desticationFile):
  csv = genfromtxt (fileName, delimiter=",")
  dataColumn = csv[:,column]
  writeFinalDatatxt(desticationFile, dataColumn)
  return dataColumn


# ------------------
# Function write Individual data
# ------------------
def writeFinalDatatxt (desticationFile, dataToSave):
  with open(desticationFile, 'w') as f:
    for data in dataToSave:
        f.write("%s\n" % data)


# ------------------
# Function convert today date
# ------------------
def convertTodayDate():
  todayPlus1 = date.today() + timedelta(days=1)
  year = todayPlus1.strftime("%Y")
  month = todayPlus1.strftime("%B")
  day = todayPlus1.strftime("%d")
  endDate = day + " " + month + ", " + year
  return endDate
  

# ------------------
# Function date time to timestamp
# ------------------
def dateTime_Timestamp(signalDate, signalTime):
  
  signalDateTime = signalDate + " " + signalTime + "00"
  date_time_obj = datetime.strptime(signalDateTime, '%d %B, %Y %H%M%S')
  timestamp = datetime.timestamp(date_time_obj)
  #This timestamp has less 0s than binance timestamp so adding more 0s
  #print(str(timestamp) + "info timestamp **********")
  #timestampModified_str = str(math.trunc(timestamp)) + "000"
  #timestampModified_int = int(timestampModified_str)
  #print(str(timestamp*1000) + "info timestamp **********")
  #print(signalDate + " " + signalTime)
  return (timestamp*1000)



# ------------------
# Function timestamp to DateTime
# ------------------
def Timestamp_dateTime(timestamp):
  #print(str(timestamp) + " time stamp")
  dt_object = datetime.fromtimestamp(timestamp/1000)
  return dt_object


# ------------------
# Function convert userinput date
# ------------------
def convertInputDate(inputDate):
  
  convertedDate = datetime.strptime(inputDate,'%Y%m%d').date()
  #endDate = convertedDate.day + " " + convertedDate.month + ", " + convertedDate.year
  #print(type(convertedDate) + "    " + convertedDate2.year)
  monthInWords = str(convertedDate.strftime('%B'))
  endDate = str(convertedDate.day) + " " + str(monthInWords)+ ", " + str(convertedDate.year)
  return endDate

# ------------------
# Function save signal data
# ------------------
def SavesignalData(SigName, entryPri, leverage, tp1, tp2, tp3, tp4, stoploss, tradeType, signalDate, signalTime):
  
  filename = SigName + tradeType + ".txt"
  
  if os.path.isfile(filename):
    #print ("File exist")
    print("")
  else:
    open(filename, 'a').close()
    #print(filename + " created empty")

  with open (filename, 'wb') as outp:
    p1 = SignalObject.Signal(SigName, entryPri, leverage, tp1, tp2, tp3, tp4, stoploss, tradeType, signalDate, signalTime)
    pickle.dump(p1, outp, pickle.HIGHEST_PROTOCOL)
  del p1


# ------------------
# Function add new signal
# ------------------
def addNewSignal():
  SigName = input("Coin Name: ")
  entryPri = input("Entry price: ")
  leverage = input("Leverage: ")
  tp1 = input("tp1: ")
  tp2 = input("tp2: ")
  tp3 = input("tp3: ")
  tp4 = input("tp4: ")
  stoploss = input("Stoploss: ")
  tradeType = input("Trade Type: ")
  tempStartDate = input("Signal Date (20211201): ")
  signalTime = input("Signal time: ")

  signalDate = convertInputDate(tempStartDate)
  endDate = convertTodayDate()

  SavesignalData(SigName, entryPri, leverage, tp1, tp2, tp3, tp4, stoploss, tradeType, signalDate, signalTime)


# ------------------
# Function saved get signal info
# ------------------
def getSavedSignals():
  SigName = input("Coin Name: ")
  tradeType = input("Trade Type: ")
  filename = SigName + tradeType + ".txt"
  print(filename)
  # fileContent = pickle.load( open( filename, "rb" ))

  if os.path.isfile(filename):
    if os.path.getsize(filename) > 0:      
      
      with open(filename, 'rb') as inp:
        p1 = pickle.load(inp)
        #print(p1.SigName, p1.entryPri, p1.leverage, p1.tp1, p1.tp2, p1.tp3, p1.tp4, p1.stoploss, p1.tradeType, p1.signalDate)

    else: print("file size < 0")
  else: print("File not found!!")


# ------------------
# Function saved get signal info **2***
# ------------------
def getSavedSignals2(filename):
  # fileContent = pickle.load( open( filename, "rb" ))

  if os.path.isfile(filename):
    if os.path.getsize(filename) > 0:      
      
      with open(filename, 'rb') as inp:
        p1 = pickle.load(inp)
        return p1
        #print(p1.SigName, p1.entryPri, p1.leverage, p1.tp1, p1.tp2, p1.tp3, p1.tp4, p1.stoploss, p1.tradeType, p1.signalDate)

    else: print("file size < 0")
  else: print("File not found!!")

# ------------------
# Function view all saved signals
# ------------------
def viewAllSavedSignals():
  workingPath = os.getcwd()
  searchstring = "USDT"

  txtFiles = []

  for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.txt'):
      if "USDT" in file:
        txtFiles.append(file)
        print(file)

  if len(txtFiles) == 0:
    #print(Fore.WHITE + "No files with 'USDT' in it"  + Style.RESET_ALL)
    return 0
  elif len(txtFiles) > 0:
    return txtFiles
      


# ------------------
# Function candles manager
# ------------------
def modifyCoinName(savedCoinName):
  substr = "USDT"
  inserttxt = "/"

  idx = savedCoinName.index(substr)
  my_str = savedCoinName[:idx] + inserttxt + savedCoinName[idx:]
  return my_str


# ------------------
# Function takeprofit & stoploss checker
# ------------------
def tp_sl_checker():

  signalFilesList = viewAllSavedSignals()  

  #clearing the list before start
  postedSignalList.clear()   
  n = postedSignalCheck("read", "N/A", "N/A")
  
  if signalFilesList != 0:
    for filename in signalFilesList:
      signalDataFromFile = getSavedSignals2(filename)
      print(Fore.GREEN + "\n\n \033[4m Signal " + str(signalDataFromFile.SigName) + "\033[0m" + Style.RESET_ALL)
      candleManager(signalDataFromFile)
      
  n = postedSignalCheck("write", "N/A", "N/A")
  #clearing the list at end
  postedSignalList.clear() 
      



# ------------------
# Function candles manager
# ------------------
def candleManager(signalDataFromFile):
  endDate = convertTodayDate()

  candleDataFile = 'candlesticks.csv'
  timeStampFile = 'timeStamp.txt'
  candleHighFile = 'candleHigh.txt'
  candleLowFile = 'candleLow.txt'

  

  #deleting candle data file
  deleteFiles(candleDataFile)

  deleteFiles(timeStampFile)
  createFiles(timeStampFile)

  deleteFiles(candleHighFile)
  createFiles(candleHighFile)

  deleteFiles(candleLowFile)
  createFiles(candleLowFile)

  getCandleData(signalDataFromFile.SigName,"candlesticks.csv", signalDataFromFile.signalDate, endDate)

  signalDate_Timestamp = dateTime_Timestamp(signalDataFromFile.signalDate, signalDataFromFile.signalTime)

  ModifiedCoinName = modifyCoinName(signalDataFromFile.SigName)

  timestampData = getIndividualData(0, candleDataFile, timeStampFile)
  highData  = getIndividualData(2, candleDataFile, candleHighFile)
  lowData = getIndividualData(3, candleDataFile, candleLowFile)

  #print("Original ---- " + str(signalDate_Timestamp))

  if(signalDataFromFile.tradeType == "LONG"):
    tp_sl_cal_long(signalDataFromFile, timestampData, highData, lowData, ModifiedCoinName, signalDate_Timestamp)
  
  if(signalDataFromFile.tradeType == "SHORT"):
    tp_sl_cal_short(signalDataFromFile, timestampData, highData, lowData, ModifiedCoinName, signalDate_Timestamp)





# ------------------
# Function Tp/SL checker
# ------------------
def tp_sl_cal_long(signalDataFromFile, timestampData, highData, lowData, ModifiedCoinName, signalDate_Timestamp):

  dateFoundBool = False
  falseDatesCount = 0

  #counting how much wrong timestamps there are before the actual signal is started. 
  for timestamp in timestampData:
    if dateFoundBool == False and (timestamp>signalDate_Timestamp) :
      dateFoundBool = True
      #print(timestamp)
  
    if dateFoundBool == False:
      falseDatesCount += 1

  tp1HitPos, tp2HitPos, tp3HitPos, tp4HitPos = 0, 0, 0, 0
  tp1HitBool, tp2HitBool, tp3HitBool, tp4HitBool, signalInvalid, slHitBool, alreadyDoneSignal = False, False, False, False, False, False, False
  tp1Message, tp1Message, tp1Message, tp1Message = "", "", "", ""

  
  count = 0
  for high in highData:
    if count >= falseDatesCount:
        
      if float(high) >= float(signalDataFromFile.tp1) and tp1HitBool == False and float(signalDataFromFile.tp1) > float(signalDataFromFile.entryPri):
        alreadyDoneSignal = postedSignalCheck("add", ModifiedCoinName, "tp1")
        tp1HitPos = count
        tp1HitBool = True

        if(alreadyDoneSignal == False):
          tp1Message = "Binance Futures \n#" + str(ModifiedCoinName) + " Take-Profit Target 1 ✅"
          print(Fore.YELLOW +"\n" + tp1Message  + Style.RESET_ALL)
          ProfitPercentageCal(signalDataFromFile, signalDataFromFile.tp1)
          tpPeriodCalculator(timestampData, tp1HitPos, signalDataFromFile)
        
        

      if float(high) >= float(signalDataFromFile.tp2) and tp2HitBool == False and float(signalDataFromFile.tp2) > float(signalDataFromFile.entryPri):
        alreadyDoneSignal = postedSignalCheck("add", ModifiedCoinName, "tp2")
        tp2HitPos = count
        tp2HitBool = True

        if(alreadyDoneSignal == False):
          tp2Message = "Binance Futures \n#" + str(ModifiedCoinName) + " Take-Profit Target 2 ✅" 
          print(Fore.YELLOW +"\n"  + tp2Message  + Style.RESET_ALL) 
          ProfitPercentageCal(signalDataFromFile, signalDataFromFile.tp2)
          tpPeriodCalculator(timestampData, tp2HitPos, signalDataFromFile)
        
        
         
      if float(high) >= float(signalDataFromFile.tp3) and tp3HitBool == False and float(signalDataFromFile.tp3) > float(signalDataFromFile.entryPri):
        alreadyDoneSignal = postedSignalCheck("add", ModifiedCoinName, "tp3")
        tp3HitPos = count
        tp3HitBool = True

        if(alreadyDoneSignal == False):
          tp3Message = "Binance Futures \n#" +str(ModifiedCoinName) + " All Take-Profit Targets achieved 😎💰" 
          print(Fore.YELLOW +"\n"  + tp3Message  + Style.RESET_ALL)
          ProfitPercentageCal(signalDataFromFile, signalDataFromFile.tp3)
          tpPeriodCalculator(timestampData, tp3HitPos, signalDataFromFile)
        
        

      if float(high) >= float(signalDataFromFile.tp4) and tp4HitBool == False and float(signalDataFromFile.tp4) > float(signalDataFromFile.entryPri):
        alreadyDoneSignal = postedSignalCheck("add", ModifiedCoinName, "tp4")
        tp4HitPos = count
        tp4HitBool = True

        if(alreadyDoneSignal == False):
          tp4Message = "Binance Futures \n#" + str(ModifiedCoinName) + " Take-Profit Target 4 ✅" 
          print(Fore.YELLOW +"\n"  + tp4Message  + Style.RESET_ALL) 
          ProfitPercentageCal(signalDataFromFile, signalDataFromFile.tp4)
          tpPeriodCalculator(timestampData, tp4HitPos, signalDataFromFile)

             #and tp1HitBool == False and tp2HitBool == False and tp3HitBool == False and tp4HitBool == False
      if(slHitBool == False):
        slHitBool = stoplossChecker(timestampData, signalDate_Timestamp, lowData, highData, signalDataFromFile, ModifiedCoinName, tp1HitBool, tp2HitBool, tp3HitBool, tp4HitBool, count)

      # #Checking for invalid signals after hitting tp1
      # if tp1HitBool == True and signalInvalid == False:
      #   i = count
      #   for low in lowData:

      #     if i == falseDatesCount and float(low) <= float(signalDataFromFile.entryPri) and signalInvalid == False:
      #       signalInvalid = True
      #       print(Fore.LIGHTRED_EX +"\n"  + "Signal Invalid: Back to SL from TP " + Style.RESET_ALL)

      #     i += 1

    count += 1

  


def tp_sl_cal_short(signalDataFromFile, timestampData, highData, lowData, ModifiedCoinName, signalDate_Timestamp):

  dateFoundBool = False
  falseDatesCount = 0

  #counting how much wrong timestamps there are before the actual signal is started. 
  for timestamp in timestampData:
    if dateFoundBool == False and (timestamp>signalDate_Timestamp) :
      dateFoundBool = True
      #print(timestamp)
  
    if dateFoundBool == False:
      falseDatesCount += 1

  tp1HitPos, tp2HitPos, tp3HitPos, tp4HitPos = 0, 0, 0, 0
  tp1HitBool, tp2HitBool, tp3HitBool, tp4HitBool, signalInvalid, slHitBool, alreadyDoneSignal = False, False, False, False, False, False, False
  tp1Message, tp1Message, tp1Message, tp1Message = "", "", "", ""
   

  count = 0
  for low in lowData:
    if count >= falseDatesCount:
        
      if float(low) <= float(signalDataFromFile.tp1) and tp1HitBool == False and float(signalDataFromFile.tp1) < float(signalDataFromFile.entryPri):
        alreadyDoneSignal = postedSignalCheck("add", ModifiedCoinName, "tp1")
        tp1HitPos = count
        tp1HitBool = True

        if(alreadyDoneSignal == False):
          tp1Message = "Binance Futures \n#" + str(ModifiedCoinName) + " Take-Profit Target 1 ✅" 
          print(Fore.YELLOW +"\n"  + tp1Message  + Style.RESET_ALL)
          ProfitPercentageCal(signalDataFromFile, signalDataFromFile.tp1)
          tpPeriodCalculator(timestampData, tp1HitPos, signalDataFromFile)
        

      if float(low) <= float(signalDataFromFile.tp2) and tp2HitBool == False and float(signalDataFromFile.tp2) < float(signalDataFromFile.entryPri):
        alreadyDoneSignal = postedSignalCheck("add", ModifiedCoinName, "tp2")
        tp2HitPos = count
        tp2HitBool = True

        if(alreadyDoneSignal == False):
          tp2Message = "Binance Futures \n#" + str(ModifiedCoinName) + " Take-Profit Target 2 ✅" 
          print(Fore.YELLOW +"\n"  + tp2Message  + Style.RESET_ALL) 
          ProfitPercentageCal(signalDataFromFile, signalDataFromFile.tp2)
          tpPeriodCalculator(timestampData, tp2HitPos, signalDataFromFile)
         
      if float(low) <= float(signalDataFromFile.tp3) and tp3HitBool == False and float(signalDataFromFile.tp3) < float(signalDataFromFile.entryPri):
        alreadyDoneSignal = postedSignalCheck("add", ModifiedCoinName, "tp3")
        tp3HitPos = count
        tp3HitBool = True

        if(alreadyDoneSignal == False):
          tp3Message = "Binance Futures \n#" +str(ModifiedCoinName) + " All Take-Profit Targets achieved 😎💰" 
          print(Fore.YELLOW +"\n"  + tp3Message  + Style.RESET_ALL)
          ProfitPercentageCal(signalDataFromFile, signalDataFromFile.tp3)
          tpPeriodCalculator(timestampData, tp3HitPos, signalDataFromFile)

      if float(low) <= float(signalDataFromFile.tp4) and tp4HitBool == False and float(signalDataFromFile.tp4) < float(signalDataFromFile.entryPri):
        alreadyDoneSignal = postedSignalCheck("add", ModifiedCoinName, "tp4")
        tp4HitPos = count
        tp4HitBool = True

        if(alreadyDoneSignal == False):
          tp4Message = "Binance Futures \n#" + str(ModifiedCoinName) + " Take-Profit Target 4 ✅" 
          print(Fore.YELLOW +"\n"  + tp4Message  + Style.RESET_ALL)
          ProfitPercentageCal(signalDataFromFile, signalDataFromFile.tp4)
          tpPeriodCalculator(timestampData, tp4HitPos, signalDataFromFile) 


      if(slHitBool == False):
        slHitBool = stoplossChecker(timestampData, signalDate_Timestamp, lowData, highData, signalDataFromFile, ModifiedCoinName, tp1HitBool, tp2HitBool, tp3HitBool, tp4HitBool, count)

      # if tp1HitBool == True and signalInvalid == False:
      #   for high in highData:
      #     i = 0

      #     if i >= falseDatesCount and float(high) >= float(signalDataFromFile.entryPri) and signalInvalid == False:
      #       signalInvalid = True
      #       print(Fore.LIGHTRED_EX +"\n"  + "Signal Invalid: Back to entry from TP1 " + Style.RESET_ALL)

      #     i += 1


    count += 1

  



# ------------------
# Function signal tp period calculator
# ------------------
def tpPeriodCalculator(timestampData, tp1HitPos, signalDataFromFile):
  i = 0
  for timestamp in timestampData:
    if i == tp1HitPos:
      tpDateTime = Timestamp_dateTime(timestamp)
      
      signalDateTime = signalDataFromFile.signalDate + " " + signalDataFromFile.signalTime + "00"
      SigDateTimeFormatted = datetime.strptime(signalDateTime, '%d %B, %Y %H%M%S')

      
      differeceTime = tpDateTime - SigDateTimeFormatted
      days, seconds = differeceTime.days, differeceTime.seconds
      Hours = seconds // 3600
      minutes = (seconds//60)%60
      
      print(Fore.YELLOW +  "Period: " + str(days) + " Day(s) " + str(Hours) + " Hour(s) " + str(minutes) + " Minute(s) ⏰" + Style.RESET_ALL)
    i += 1


# ------------------
# Function signal tp profit percentage cal
# ------------------
def ProfitPercentageCal(signalDataFromFile, tp):
  if(signalDataFromFile.tradeType == "LONG"):
    _1x_percentage = (100/float(signalDataFromFile.entryPri)) * (float(tp) - float(signalDataFromFile.entryPri))
    leverageProfit = float(_1x_percentage) * float(signalDataFromFile.leverage)
    print(Fore.YELLOW + "Profit: " + str(round(leverageProfit, 2)) +"% with " + signalDataFromFile.leverage + "x" + Style.RESET_ALL)


  if(signalDataFromFile.tradeType == "SHORT"):
    _1x_percentage = (100/float(signalDataFromFile.entryPri)) * (float(signalDataFromFile.entryPri) - float(tp))
    #print(signalDataFromFile.entryPri + "    signalDataFromFile.entryPri")
    #print(tp + "      tp")
    #print(_1x_percentage + "     _1x_percentage")
    leverageProfit = float(_1x_percentage) * float(signalDataFromFile.leverage)
    #print(leverageProfit + "     leverageProfit")
    print(Fore.YELLOW + "Profit: " + str(round(leverageProfit, 2)) +"% with " + signalDataFromFile.leverage + "x" + Style.RESET_ALL)



# ------------------
# Function stoploss calculator
# ------------------
def stoplossChecker(timestampData, signalDate_Timestamp, lowData, highData, signalDataFromFile, ModifiedCoinName, tp1HitBool, tp2HitBool, tp3HitBool, tp4HitBool, count):
  dateFoundBool = False
  falseDatesCount = 0

  #counting how much wrong timestamps there are before the actual signal is started. 
  for timestamp in timestampData:
    if dateFoundBool == False and (timestamp>signalDate_Timestamp):
      dateFoundBool = True
  
    if dateFoundBool == False:
      falseDatesCount += 1

  slHitBool = False
  currentLowFound = False
  currentLow = 0
  currentHigh = 0
  i = 0

  
  

  if(signalDataFromFile.tradeType == "LONG"):

    for low in lowData:
      if i == count:
        currentLow = low
      i += 1

    if float(currentLow) <= float(signalDataFromFile.stoploss) and slHitBool == False and signalDataFromFile.stoploss < signalDataFromFile.entryPri:
      slHitBool = True
      stoplossMsg = "\nBinance Futures \n#" + str(ModifiedCoinName) + " Stop Loss ⛔️" 
      print(Fore.LIGHTRED_EX + stoplossMsg  + Style.RESET_ALL)

      #SL calculator
      _1x_percentage = (100/float(signalDataFromFile.entryPri)) * (float(signalDataFromFile.entryPri) - float(signalDataFromFile.stoploss))
      leverageProfit = float(_1x_percentage) * float(signalDataFromFile.leverage)
      print(Fore.LIGHTRED_EX + "Loss: -" + str(round(leverageProfit, 2)) +"% with " + signalDataFromFile.leverage + "x" + Style.RESET_ALL)



  if(signalDataFromFile.tradeType == "SHORT"):

    for high in highData:
      if i == count:
        currentHigh = high
      i += 1

    if float(currentHigh) >= float(signalDataFromFile.stoploss) and slHitBool == False and signalDataFromFile.stoploss > signalDataFromFile.entryPri:
      slHitBool = True
      stoplossMsg = "\nBinance Futures \n#" + str(ModifiedCoinName) + " Stop Loss ⛔️" 
      print(Fore.LIGHTRED_EX + stoplossMsg  + Style.RESET_ALL)

      #SL calculator
      _1x_percentage = (100/float(signalDataFromFile.entryPri)) * (float(signalDataFromFile.entryPri) - float(signalDataFromFile.stoploss))
      leverageProfit = float(_1x_percentage) * float(signalDataFromFile.leverage)
      print(Fore.LIGHTRED_EX + "Loss: " + str(round(leverageProfit, 2)) +"% with " + signalDataFromFile.leverage + "x" + Style.RESET_ALL)


  return slHitBool




# ------------------
# Function edit signal details
# ------------------
def signalEditor():

  listOfSignals = viewAllSavedSignals()
  SigFileToEdit = input(Fore.CYAN + "Signal file to edit" + Style.RESET_ALL)
  p1 = None

  #reading file for edit
  for file in listOfSignals:
    if str(file) == SigFileToEdit:
  
      signalDataFromFile = getSavedSignals2(file)
      print(Fore.GREEN + "\n\n \033[4m Editing Signal " + str(signalDataFromFile.SigName) + ".... \033[0m" + Style.RESET_ALL)
      p1 = SignalObject.Signal(signalDataFromFile.SigName, signalDataFromFile.entryPri, signalDataFromFile.leverage, signalDataFromFile.tp1, signalDataFromFile.tp2, signalDataFromFile.tp3, signalDataFromFile.tp4, signalDataFromFile.stoploss, signalDataFromFile.tradeType, signalDataFromFile.signalDate, signalDataFromFile.signalTime)
        
  #Editing the object p1
  loop = False
  while loop == False:
    ValueToEdit = input(Fore.CYAN + "What do you want to edit: n/" + Style.RESET_ALL)
    if(ValueToEdit == ""):
      loop = True
    else:
      inputValue = input(Fore.CYAN + "Enter value: \n" + Style.RESET_ALL)
      
      if(ValueToEdit == "entryPri"):
        p1.entryPri =  inputValue
      if(ValueToEdit == "tp1"):
        p1.tp1 =  inputValue
      if(ValueToEdit == "tp2"):
        p1.tp2 =  inputValue
      if(ValueToEdit == "tp3"):
        p1.tp3 =  inputValue
      if(ValueToEdit == "tp4"):
        p1.tp4 =  inputValue
      if(ValueToEdit == "stoploss"):
        p1.stoploss =  inputValue


  with open (SigFileToEdit, 'wb') as outp:
      pickle.dump(p1, outp, pickle.HIGHEST_PROTOCOL)
  del p1



# ------------------
# Function PostedSignalCheck
# ------------------
def postedSignalCheck(option, signalName, tp):
  # print("initial function - " + signalName + tp)
  global postedSignalList

  fileName = 'postedSignalCheck.txt'
  signalDublicate = False


  #add to list
  if option == "add":
    #print("in add statement - " + signalName + tp)
    if len(postedSignalList) != 0:
      for item in postedSignalList:
        if(signalName in item and tp in item):
          signalDublicate = True
          return True
      
    
    if signalDublicate == False:
      data1 = str(signalName) + " " + str(tp)
      postedSignalList.append(data1)
      return False

  # #check from the list
  # if option == "check":
  #   for item in postedSignalList:
  #     if signalName in item and tp in item:
  #       return True


  # #read file
  if option == "read":

    if os.path.exists(fileName):
      print("")
    else:
      open(fileName, 'w').close()
      print(fileName + " created")  

    file = open(fileName, 'r')
    dataList = file.readlines()
    content = [x.strip() for x in dataList]

    for item in content:
      postedSignalList.append(item)
      print(item)


  #write to file
  if option == "write":
      
    # for item in postedSignalList:
    # if os.path.exists(fileName):
    #   os.remove(fileName)
    #   print(fileName + " removed")
    #   open(fileName, 'a').close()
    #   print(fileName + " created")
    # else:
    #   print(Fore.LIGHTRED_EX + fileName + " does not exist" + Style.RESET_ALL)

    with open(fileName, 'w') as f:
      for data in postedSignalList:
        #if(data != "" or data != " "):
        f.write("%s\n" % data)

