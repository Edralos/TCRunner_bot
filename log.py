import requests


logFileName = None
logFile = None
discordWebHookUrl = None

##File



def setlogFile(logFileName):
    if logFile is not None:
        logFile.close()
    logFile = open(logFileName, "a")
    logFileName = logFileName
    return
    
def closelogFile():
    if logFile is not None:
        logFile.close()
    logFileName = None
    return

def writeInitLogFile(config):
    try:
        #list of strategies
        strats = config["strategies"]
        config.pop["strategies"]
        
        file.write("Config:\n")
        #global config
        for k,v in config.items():
            file.write(k + " : " + str(v) + "\n")
        file.write("\nCurrency config:\n")
        for i in strats:
            for k,v in strats[i]:
                file.write("\t" + k + " : " + str(v) + "\n")
            file.write("\n")
        file.write("\n\n")
        
    except:
        print("error logfile")
    finally:
        return

def writeFileNecklineReached(neckType, currency, val):
    try:
        file.write( "Neckline " + neckType + " ("+ str(val) + ") reached for :" + currency + "\nNext neckline breach won't be considered until units of this currency are sold\n")
    except:
        print("error logfile")
    finally:
        return

def writeFileLoan(currency, amount):
    try:
        file.write("loan : " + str(amount) + " " + currency)
    except:
        print("error logfile")
    finally:
        return
        
    

def writeFileText(txt):
    try:
        file.write(txt + "\n")
    except:
        print("error logfile")
    finally:
        return
    

