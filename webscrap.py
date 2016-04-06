import requests
from bs4 import BeautifulSoup

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


URL = ["http://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/torrentpharmaceuticals/TP06",
        "http://www.moneycontrol.com/india/stockpricequote/refineries/indianoilcorporation/IOC",
        "http://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT",
        "http://www.moneycontrol.com/india/stockpricequote/computers-software/tataconsultancyservices/TCS"]

def getStockDetails(url):
    page = requests.get(url).text
    #Bse_Prc_tick
    soup = BeautifulSoup(page,"html.parser")
    bseVal = soup.select("#Bse_Prc_tick strong")[0].contents[0]
    nseVal = soup.select("#Nse_Prc_tick strong")[0].contents[0]
    riseBseVal = soup.select("#b_changetext strong")[0].contents[0]
    riseNseVal = soup.select("#n_changetext strong")[0].contents[0]
    directionBse = soup.find('div',id="b_changetext").span['class']
    directionNse = soup.find('div',id="n_changetext").span['class']
    sentiments_buy = sentiments_sell = sentiments_hold = colorBse = colorNse = ''
    title = soup.find('h1','b_42').contents[0]
    try:
        sentiments_buy = soup.find('span','pl_bar brdwr')['style'].replace('width:','')
    except:
        sentiments_buy = ''
    try:
        sentiments_sell = soup.find('span','pl_bar brdwr rd')['style'].replace('width:','')
    except:
        sentiments_sell = ''
    try:
        sentiments_hold = soup.find('span','pl_bar hold')['style'].replace('width:','')
    except:
        sentiments_hold = ''
    sentiments = ''

    if 'uparw_pc' in directionBse:
        directionBse = 'UP'
        colorBse = bcolors.OKGREEN
    else:
        directionBse = 'DOWN'
        colorBse = bcolors.FAIL

    if 'uparw_pc' in directionNse:
        directionNse = 'UP'
        colorNse = bcolors.OKGREEN
    else:
        directionNse = 'DOWN'
        colorNse = bcolors.FAIL

    if sentiments_buy is not 'None' and sentiments_buy is not '':
        sentiments =  sentiments + bcolors.OKGREEN + sentiments_buy + bcolors.ENDC +" "

    if sentiments_hold is not 'None' and sentiments_hold is not '':
        sentiments =  sentiments + bcolors.WARNING + sentiments_hold + bcolors.ENDC +" "

    if sentiments_sell is not 'None' and sentiments_sell is not '':
        sentiments =  sentiments + bcolors.FAIL + sentiments_sell + bcolors.ENDC +" "

    print(bcolors.BOLD+ title+ bcolors.ENDC)
    print ("BSE: "+bseVal +" "+ colorBse + riseBseVal + bcolors.ENDC + " "+ directionBse)

    print ("NSE: "+nseVal +" "+ colorNse +riseNseVal + bcolors.ENDC + " "+ directionNse)
    if sentiments is not '':
        print("Sentiments: " + sentiments )

    print ('\n')

for url in URL:
    getStockDetails(url)

#def analysis(url):
