import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

req = requests.get("http://www.forexfactory.com/calendar.php?day=tomorrow")
soup = BeautifulSoup(req.content,"lxml")
forexcalendarTable = soup.find_all("div",{"id":"flexBox_flex_calendar_mainCal"})[0]
root = ET.Element('root')
dateVal = ''
timeVal = ''
currDictionary = {}
for table in forexcalendarTable.find_all('table')[14:]:
    for tr in table.find_all('tr')[2:]:
        if tr.contents[1].text != '':
            dateVal = tr.contents[1].text
        if tr.contents[3].text != '':
            timeVal = tr.contents[3].text
        if tr.contents[5].text not in currDictionary and tr.contents[5].text != '':
            currDictionary.update({tr.contents[5].text:ET.SubElement(root, 'currency', id=tr.contents[5].text)})
        if currDictionary:
            ET.SubElement(currDictionary[tr.contents[5].text], tr.contents[5].text,Value=("Date=%s,Time=%s,Impact=%s,Economic_News=%s,Actual=%s,Forecast=%s,Previous=%s")
                        %(dateVal,timeVal,tr.contents[7].find("span")["title"],tr.contents[9].text,tr.contents[13].text,tr.contents[15].text,tr.contents[17].text))    
tree = ET.ElementTree(root) 
tree.write("forexCalendarTomorrow.xml")
