import discord
from DiscordBot import DBot

logFileName = None
logFile = None
bot = None

##File



def setlogFile(logfileName):
    global logFile
    if logFile is not None:
        logFile.close()
    global logFileName
    logFile = open(logfileName, "a")
    logFileName = logfileName
    return

def closelogFile():
    global logFile
    if logFile is not None:
        logFile.close()
    global logFileName
    logFileName = None
    return

def _writeInitLogFile(config):
    try:
        #list of strategies
        strats = config["strategies"]
        config.pop["strategies"]

        logFile.write("Config:\n")
        #global config
        for k,v in config.items():
            logFile.write(k + " : " + str(v) + "\n")
        logFile.write("\nCurrency config:\n")
        for i in strats:
            for k,v in strats[i]:
                logFile.write("\t" + k + " : " + str(v) + "\n")
            logFile.write("\n")
        logFile.write("\n\n")

    except:
        print("error logfile")
    finally:
        return

def _writeFileNecklineReached(neckType, currency, val):
    try:
        logFile.write( "Neckline " + neckType + " ("+ str(val) + ") reached for :" + currency + "\nNext neckline breach won't be considered until units of this currency are sold\n")
    except:
        print("error logfile")
    finally:
        return

def _writeFileLoan(currency, amount):
    try:
        logFile.write("loan : " + str(amount) + " " + currency)
    except:
        print("error logfile")
    finally:
        return



def _writeFileText(txt):
    try:
        logFile.write(txt + "\n")
    except:
        print("error logfile")
    finally:
        return

def _writeFilePurchase(amount, cost, cryptoCurrency, exchangeCurrency):
    try:
        logFile.write("Purchase : " + str(amount) + " " +cryptoCurrency + " for " + str(cost) + " " + exchangeCurrency+ "\n")
    except:
        print("error logfile")
    finally:
        return


def _writeFileSale(amount, cryptoCurrency, benefits, exchangeCurrency, percentageDifference):
    try:
        if percentageDifference <0:
            sign = "-"
        else:
            sign = "+"
        logFile.write("Sold : " + str(amount) + " " + cryptoCurrency + " for " + str(benefits) +" " + exchangeCurrency + " " + sign + str(percentageDifference) + "%")
    except:
        print("error logfile")
    finally:
        return


def _writeFileResume(ignoredCurrencies):
    try:
        st = ""
        for i in ignoredCurrencies:
            st += ignoredCurrencies[i] + " "
        logFile.write("Resuming. Ignored currencies are : " + st)
    except:
        print("error logfile")
    finally:
        return

##Discord Webhook

def setDiscordBot(token, prefix=None):
    global bot
    bot = DBot(command_prefix = prefix, token = token)


def _writeDiscordText(text):
    bot.sendText(text)
    return

def _writeInitLogDiscord(config):
    res = "Config :\n"
    #list of strategies
    strats = config["strategies"]
    config.pop["strategies"]

    #global config
    for k,v in config.items():
        res += k + " : " + str(v) + "\n"
    logFile.write("\nCurrency config:\n")
    for i in strats:
        for k,v in strats[i]:
            res += "\t" + k + " : " + str(v) + "\n"
        res += "\n"
    _writeDiscordText(res)
    
def _writeDiscordNecklineReached(neckType, currency, val):
    field = {"Type": neckType, "Neckline value": str(val), "Currency": currency}
    bot.sendEmbed(content="Next neckline breach won't be considered until units of this currency are sold",title="Neckline passed",description= bot.MENTION,fields = field, color = 0x1ab6cb )



def _writeDiscordLoan(currency, amount):
    fields = {"Borrowed": str(amount)+" " + currency}
    bot.sendEmbed(title="Loan", description=bot.MENTION, fields = fields, color= 0xd6ff42)

def _writeDiscordPurchase(amount, cost, cryptoCurrency, exchangeCurrency):
    fields = {"Purchased": str(amount)+" " + cryptoCurrency, "Cost": str(cost)+" "+exchangeCurrency}
    bot.sendEmbed(title="Purchase", description=bot.MENTION, fields=fields, color=0xd6ff42)

def _writeDiscordSale(amount, cryptoCurrency, benefits, exchangeCurrency, percentageDifference):
    if percentageDifference < 0:
        color = 0xff1414
    else:
        color = 0x19f032
    fields = {"Sold": str(amount)+" "+cryptoCurrency, "Sold for": str(benefits)+" "+exchangeCurrency, "Percentage": "```diff\n"+str(percentageDifference) + "%\n```"}
    bot.sendEmbed(title="Sale", description=bot.MENTION, fields=fields, color=color)


def _writeDiscordResume(ignoredCurrencies):
    st = ""
    for i in ignoredCurrencies:
        st += ignoredCurrencies[i] + " "
    bot.sendText(bot.MENTION+" Resuming. Ignored currencies are: "+ st)