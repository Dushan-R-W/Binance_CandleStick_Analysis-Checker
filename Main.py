from binance.client import Client
from numpy import genfromtxt
import os
from datetime import datetime, timedelta
import functions
from datetime import date
import sys
from colorama import Fore, Back, Style
from os import system, name

#gettinguser input choice

loop = False
while loop == False:
    print("\n\n *****************************************")
    print("Last run time - " + str(datetime.today().time()))
    print(" *****************************************")
    SigName = input(Fore.CYAN + "1 - Add new signal \n2 - Edit Signal \n3 - View all saved signals\n4 - Tp/SL checker\n5 - EXIT\n\n" + Style.RESET_ALL)
    
    if SigName == "1":
        functions.addNewSignal()
    elif SigName == "2":
        functions.signalEditor()
    elif SigName == "3":
        signals = functions.viewAllSavedSignals()
    elif SigName == "4":
        functions.tp_sl_checker()
    # elif SigName == "5":
    #     sys.exit()
    # elif SigName == "6":
    #     os.system('cls') 
    #     sys.exit()
    elif SigName == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()
    else:
        sys.exit()
    
         
