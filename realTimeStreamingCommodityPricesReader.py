import requests
import lxml.etree
import lxml.builder
import xml.etree.cElementTree as ET
from bs4 import BeautifulSoup

tableIdDictionary = {'1':'cross_rate_1', '2':'marketsPerformance', '3':'marketsTechnical','4':'specifications'}

def writeCommodityPrice(category,fileName,url,session1):
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
    COMMODITY = E.commodity
    MONTH = E.month
    LAST = E.last
    PREV = E.prev
    HIGH = E.high
    LOW = E.low
    CHG = E.chg
    CHGPERCENTAGE = E.chgpercentage
    TIME = E.time

    the_doc = ROOT()

    for elements in singleCurrencyCrossesTable:
        for tr in elements.contents[1]:
            the_doc.append(RECORD(
                COMMODITY(tr.contents[1].find_all("a")[0].text),
                MONTH(tr.contents[2].text),
                LAST(tr.contents[3].text),
                PREV(tr.contents[4].text),
                HIGH(tr.contents[5].text),
                LOW(tr.contents[6].text),
                CHG(tr.contents[7].text),
                CHGPERCENTAGE(tr.contents[8].text),
                TIME(tr.contents[9].text),
                ))       
    target.write(lxml.etree.tostring(the_doc, pretty_print=True))
    target.close() 

    
def writeCommodityPerformance(category,fileName,url,session1):
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
    COMMODITY = E.commodity
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
                COMMODITY(tr.contents[2].find_all("a")[0].text),
                DAILY(tr.contents[3].text),
                ONEWEEK(tr.contents[4].text),
                ONEMONTH(tr.contents[5].text),
                YTD(tr.contents[6].text),
                ONEYEAR(tr.contents[7].text),
                THREEYEAR(tr.contents[8].text),
                ))       
    target.write(lxml.etree.tostring(the_doc, pretty_print=True))
    target.close() 


def writeCommodityTechnical(category,fileName,url,session1):
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
    COMMODITY = E.commodity
    HOURLY = E.hourly
    DAILY = E.daily
    MONTHLY = E.monthly
    the_doc = ROOT()

    
    for elements in singleCurrencyCrossesTable:
        for tr in elements.findAll('tr')[1:]:
            the_doc.append(RECORD(
                COMMODITY(tr.contents[2].find_all("a")[0].text),
                HOURLY(tr.contents[3].text),
                DAILY(tr.contents[4].text),
                MONTHLY(tr.contents[5].text),
                ))
            
    target.write(lxml.etree.tostring(the_doc, pretty_print=True))
    target.close() 

def writeCommoditySpecifications(category,fileName,url,session1):
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
    COMMODITY = E.commodity
    SYMBOL = E.symbol
    EXCHANGE = E.exchange
    CONTRACTSIZE = E.contractsize
    MONTHS = E.months
    POINTVALUE = E.pointvalue
    the_doc = ROOT()

    
    for elements in singleCurrencyCrossesTable:
        for tr in elements.findAll('tr')[1:]:
            the_doc.append(RECORD(
                COMMODITY(tr.findAll('td')[1].text),
                SYMBOL(tr.findAll('td')[2].text),
                EXCHANGE(tr.findAll('td')[3].text),
                CONTRACTSIZE(tr.findAll('td')[4].text),
                MONTHS(tr.findAll('td')[5].text),
                POINTVALUE(tr.findAll('td')[6].text),
                ))
            
    target.write(lxml.etree.tostring(the_doc, pretty_print=True))
    target.close()

print "::::::Welcome to Real Time Streaming Commodity Prices:::::"

url1 = "http://www.investing.com/commodities/Service/Price?pairid=0&sid=1"
url2 = "http://www.investing.com/commodities/Service/Performance?pairid=0&sid=1"
url3 = "http://www.investing.com/commodities/Service/Technical?pairid=0&sid=1"
url4 = "http://www.investing.com/commodities/Service/Specifications?pairid=0&sid=1"

flNm1 = 'CommodityPrice.xml'
flNm2 = 'CommodityPerformance.xml'
flNm3 = 'CommodityTechnical.xml'
flNm4 = 'CommoditySpecifications.xml'

session1 = requests.session()
session1.headers.update({'X-Requested-With': 'XMLHttpRequest'})

writeCommodityPrice('1',flNm1,url1,session1)   
writeCommodityPerformance('2',flNm2,url2,session1)
writeCommodityTechnical('3',flNm3,url3,session1)
writeCommoditySpecifications('4',flNm4,url4,session1)
