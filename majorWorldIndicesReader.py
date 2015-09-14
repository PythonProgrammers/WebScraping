import requests
import lxml.etree
import lxml.builder
import xml.etree.cElementTree as ET
from bs4 import BeautifulSoup

tableIdDictionary = {'1':'cr_12', '2':'marketsPerformance', '3':'marketsTechnical'}

def writeIndicesPrice(category,fileName,url,session1):
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
    INDEX = E.index
    LAST = E.last
    HIGH = E.high
    LOW = E.low
    CHG = E.chg
    CHGPERCENTAGE = E.chgpercentage
    TIME = E.time

    the_doc = ROOT()

    for elements in singleCurrencyCrossesTable:
        for tr in elements.contents[1]:
            the_doc.append(RECORD(
                INDEX(tr.contents[1].find_all("a")[0].text),
                LAST(tr.contents[2].text),
                HIGH(tr.contents[3].text),
                LOW(tr.contents[4].text),
                CHG(tr.contents[5].text),
                CHGPERCENTAGE(tr.contents[6].text),
                TIME(tr.contents[7].text),
                ))       
    target.write(lxml.etree.tostring(the_doc, pretty_print=True))
    target.close() 

    
def writeIndicesPerformance(category,fileName,url,session1):
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
    INDEX = E.index
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
                INDEX(tr.contents[2].find_all("a")[0].text),
                DAILY(tr.contents[3].text),
                ONEWEEK(tr.contents[4].text),
                ONEMONTH(tr.contents[5].text),
                YTD(tr.contents[6].text),
                ONEYEAR(tr.contents[7].text),
                THREEYEAR(tr.contents[8].text),
                ))       
    target.write(lxml.etree.tostring(the_doc, pretty_print=True))
    target.close() 

def writeIndicesTechnical(category,fileName,url,session1):
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
    INDEX = E.index
    HOURLY = E.hourly
    DAILY = E.daily
    MONTHLY = E.monthly
    the_doc = ROOT()

    
    for elements in singleCurrencyCrossesTable:
        for tr in elements.findAll('tr')[1:]:
            the_doc.append(RECORD(
                INDEX(tr.contents[2].find_all("a")[0].text),
                HOURLY(tr.contents[3].text),
                DAILY(tr.contents[4].text),
                MONTHLY(tr.contents[5].text),
                ))
            
    target.write(lxml.etree.tostring(the_doc, pretty_print=True))
    target.close() 


print "::::::Welcome to Major World Indices:::::"

url1 = "http://www.investing.com/indices/Service/Price?pairid=0&sid=1"
url2 = "http://www.investing.com/indices/Service/Performance?pairid=0&sid=1"
url3 = "http://www.investing.com/indices/Service/Technical?pairid=0&sid=1"

flNm1 = 'IndicesPrice.xml'
flNm2 = 'IndicesPerformance.xml'
flNm3 = 'IndicesTechnical.xml'

session1 = requests.session()
session1.headers.update({'X-Requested-With': 'XMLHttpRequest'})

writeIndicesPrice('1',flNm1,url1,session1)   
writeIndicesPerformance('2',flNm2,url2,session1)
writeIndicesTechnical('3',flNm3,url3,session1)
