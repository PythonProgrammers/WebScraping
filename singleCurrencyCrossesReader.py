import requests
import lxml.etree
import lxml.builder
import xml.etree.cElementTree as ET
from bs4 import BeautifulSoup

top8currDictionary = {'USD':12, 'EUR':17, 'JPY':2, 'GBP':3, 'CHF':4, 'CAD':15, 'AUD':1, 'NZD':5, 'ZAR':13, 'AFN':93}
tableIdDictionary = {'1':'cr1', '2':'marketsPerformance', '3':'marketsTechnical'}

def writePriceSingleCurrency(category,fileName,url,session1):
    req = session1.get(url)
    vRequestStatus = req.status_code
    #print vRequestStatus
    if vRequestStatus == 200:
        print "Getting Response....."
    else:
        raise SystemExit("Problem getting response.Request Status:%s" % vRequestStatus)
    #print req.content

    soup = BeautifulSoup(req.content,"lxml")
    #print soup.prettify().encode('UTF-8')
    singleCurrencyCrossesTable = soup.find_all("table",{"id":tableIdDictionary[category]})
    #print singleCurrencyCrossesTable
    noOfTables = len(singleCurrencyCrossesTable)
    #print noOfTables
    if noOfTables == 1:
        print "You have rightly picked the table."
    elif noOfTables > 1:
        print "Bad HTML.Two tables with same id."
        raise SystemExit("Bad HTML.There are %d tables with same id." % noOfTables)
    elif noOfTables == 0:
        raise SystemExit("Table does not exist.")
    target = open(fileName, 'w')
    target.truncate()

    E = lxml.builder.ElementMaker()
    ROOT = E.root
    RECORD = E.record
    PAIR = E.pair
    BID = E.bid
    ASK = E.ask
    OPEN = E.open
    HIGH = E.high
    LOW = E.low
    CHG = E.chg
    CHGPERCENTAGE = E.chgpercentage
    TIME = E.time

    the_doc = ROOT()

    for elements in singleCurrencyCrossesTable:
        for tr in elements.contents[1]:
            the_doc.append(RECORD(
                PAIR(tr.contents[1].find_all("a")[0].text),
                BID(tr.contents[2].text),
                ASK(tr.contents[3].text),
                OPEN(tr.contents[4].text),
                HIGH(tr.contents[5].text),
                LOW(tr.contents[6].text),
                CHG(tr.contents[7].text),
                CHGPERCENTAGE(tr.contents[8].text),
                TIME(tr.contents[9].text),
                ))       
    target.write(lxml.etree.tostring(the_doc, pretty_print=True))
    target.close() 

    
def writePerformanceSingleCurrency(category,fileName,url,session1):
    req = session1.get(url)
    vRequestStatus = req.status_code
    #print vRequestStatus
    if vRequestStatus == 200:
        print "Getting Response....."
    else:
        raise SystemExit("Problem getting response.Request Status:%s" % vRequestStatus)
    #print req.content

    soup = BeautifulSoup(req.content.replace('\n', ''),"lxml")
    #print soup.prettify().encode('UTF-8')
    singleCurrencyCrossesTable = soup.find_all("table",{"id":tableIdDictionary[category]})
    #print singleCurrencyCrossesTable
    noOfTables = len(singleCurrencyCrossesTable)
    #print noOfTables
    if noOfTables == 1:
        print "You have rightly picked the table."
    elif noOfTables > 1:
        print "Bad HTML.Two tables with same id."
        raise SystemExit("Bad HTML.There are %d tables with same id." % noOfTables)
    elif noOfTables == 0:
        raise SystemExit("Table does not exist.")
    target = open(fileName, 'w')
    target.truncate()
    
    E = lxml.builder.ElementMaker()
    ROOT = E.root
    RECORD = E.record
    PAIR = E.pair
    DAILY = E.daily
    ONEWEEK = E.oneweek
    ONEMONTH = E.onemonth
    YTD = E.ytd
    ONEYEAR = E.oneyear
    THREEYEAR = E.threeyear
    the_doc = ROOT()

    for elements in singleCurrencyCrossesTable:
        for tr in elements.findAll('tr')[1:]:
            the_doc.append(RECORD(
                PAIR(tr.contents[2].find_all("a")[0].text),
                DAILY(tr.contents[3].text),
                ONEWEEK(tr.contents[4].text),
                ONEMONTH(tr.contents[5].text),
                YTD(tr.contents[6].text),
                ONEYEAR(tr.contents[7].text),
                THREEYEAR(tr.contents[8].text),
                ))       
    target.write(lxml.etree.tostring(the_doc, pretty_print=True))
    target.close() 


def writeTechnicalSingleCurrency(category,fileName,url,session1):
    req = session1.get(url)
    vRequestStatus = req.status_code
    #print vRequestStatus
    if vRequestStatus == 200:
        print "Getting Response....."
    else:
        raise SystemExit("Problem getting response.Request Status:%s" % vRequestStatus)
    #print req.content

    soup = BeautifulSoup(req.content.replace('\n',''),"lxml")
    #print soup.prettify().encode('UTF-8')
    singleCurrencyCrossesTable = soup.find_all("table",{"id":tableIdDictionary[category]})
    #print singleCurrencyCrossesTable
    noOfTables = len(singleCurrencyCrossesTable)
    #print noOfTables
    if noOfTables == 1:
        print "You have rightly picked the table."
    elif noOfTables > 1:
        print "Bad HTML.Two tables with same id."
        raise SystemExit("Bad HTML.There are %d tables with same id." % noOfTables)
    elif noOfTables == 0:
        raise SystemExit("Table does not exist.")
    target = open(fileName, 'w')
    target.truncate()
    
    
    E = lxml.builder.ElementMaker()
    ROOT = E.root
    RECORD = E.record
    PAIR = E.pair
    HOUR = E.hour
    DAILY = E.daily
    MONTHLY = E.monthly
    the_doc = ROOT()

    
    for elements in singleCurrencyCrossesTable:
        for tr in elements.findAll('tr')[1:]:
            the_doc.append(RECORD(
                PAIR(tr.contents[2].find_all("a")[0].text),
                HOUR(tr.contents[3].text),
                DAILY(tr.contents[4].text),
                MONTHLY(tr.contents[5].text),
                ))
            
    target.write(lxml.etree.tostring(the_doc, pretty_print=True))
    target.close() 


print "::::::Welcome to Single Currency Crosses:::::"

print "Top 8 Currency List: USD EUR JPY GBP CHF CAD AUD NZD ZAR"
print "Enter any of the currency:"
currency = raw_input()
try:
   currencyCode = top8currDictionary[currency] 
except KeyError:
    raise SystemExit("Invalid Input.Exiting program....")
url1 = "http://www.investing.com/quotes/Service/PriceSingleCurrency?pairid=%d&sid=1" % currencyCode
url2 = "http://www.investing.com/quotes/Service/PerformanceSingleCurrency?pairid=%d&sid=1" % currencyCode
url3 = "http://www.investing.com/quotes/Service/TechnicalSingleCurrency?pairid=%d&sid=1" % currencyCode

flNm1 = 'PriceSingleCurrency' + currency + '.xml'
flNm2 = 'PerformanceSingleCurrency' + currency + '.xml'
flNm3 = 'TechnicalSingleCurrency' + currency + '.xml'

session1 = requests.session()
session1.headers.update({'X-Requested-With': 'XMLHttpRequest'})

writePriceSingleCurrency('1',flNm1,url1,session1)   
writePerformanceSingleCurrency('2',flNm2,url2,session1)
writeTechnicalSingleCurrency('3',flNm3,url3,session1)
