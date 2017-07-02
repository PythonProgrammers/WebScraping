import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

req = requests.get("http://www.heromotocorp.com/en-in/the-bike/two-wheeler-motorcycles.html")
soup = BeautifulSoup(req.content,"lxml")
prodpanelTable = soup.find_all("div",{"class":"productPanel"})[0]
root = ET.Element('root')
dateVal = ''
timeVal = ''
currDictionary = {}
for a in prodpanelTable.find_all('a', href=True):
    print "Found the URL:", a['title']
    childBikeModel = ET.SubElement(root,'Model',{'text':a['title']})
    req1 = requests.get(a['href'])
    soup1 = BeautifulSoup(req1.content,"lxml")
    specsTable = soup1.find_all("div",{"class":"specsDetailsHolder"})[0]
    for a1 in specsTable.find_all('div', id=True):
		print "Found the id:", a1['id']
		childBikeModelSpecs = ET.SubElement(childBikeModel,'Spec',{'text':a1['id']})
		for row in a1.find_all('tr'):
			cells = row.find_all("td")
			rn = cells[0].get_text()
			rn1 = cells[1].get_text()
			childBikeModelSpecsProperty = ET.SubElement(childBikeModelSpecs,'Property',{'label':rn,'value':rn1})
tree = ET.ElementTree(root) 
tree.write("herobikes.xml")
