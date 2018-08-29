#standard module start
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        #bsObj.findAll(tagName, tagAttributes) 
        bsObj = BeautifulSoup(html.read(),features="html.parser")
        #findAll(tag, attributes, recursive, text, limit, keywords) 
        nameList = bsObj.findAll("span", {"class":"green"},limit=2) 
    except AttributeError as e:
        return None
    return nameList
nameList = getTitle("http://www.pythonscraping.com/pages/warandpeace.html ")
if nameList == None:
    print("Title could not be found")
else:
    for name in nameList:
        #.get_text() 会把你正在处理的 HTML 文档中所有的标签都清除
        print(name.get_text())
#standard module end      

##from urllib.request import urlopen
##from bs4 import BeautifulSoup
##html = urlopen("https://cart.jd.com/cart.action")
##bsObj = BeautifulSoup(html,features="html.parser")         
#####sibling兄弟信息
####for sibling in bsObj.find("table",{"id":"giftList"}).find("tr",{"id":"gift2"}).next_siblings:
####    print(sibling)
##print(type(bsObj.find("div",{"class":"item-full minus-item"})))
