from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
 
##html = urlopen("http://dl.stream.qqmusic.qq.com/C400003cI52o4daJJL.m4a?vkey=ED453946B0315DB9B356C21F41F95982ED9791622ADD1CE68C5EA2C29FDE33D19A438C312B065A0C2FD586C778185C0EF3F3453322FB9B21&guid=1100629362&uin=0&fromtag=66")
##bsObj = BeautifulSoup(html,features="html.parser")
##imageLocation = bsObj.find("div", {"class": "img-wrapper"}).find("img")["src"]
##urlretrieve ("http://dl.stream.qqmusic.qq.com/C400003cI52o4daJJL.m4a?vkey=ED453946B0315DB9B356C21F41F95982ED9791622ADD1CE68C5EA2C29FDE33D19A438C312B065A0C2FD586C778185C0EF3F3453322FB9B21&guid=1100629362&uin=0&fromtag=66", "logo.mp3")

musicUrl = 'http://dl.stream.qqmusic.qq.com/C400003cI52o4daJJL.m4a?vkey=ED453946B0315DB9B356C21F41F95982ED9791622ADD1CE68C5EA2C29FDE33D19A438C312B065A0C2FD586C778185C0EF3F3453322FB9B21&guid=1100629362&uin=0&fromtag=66'
req = requests.get(musicUrl.decode('utf-8'))  
with open('123.mp3'.decode('utf-8'), 'wb') as code:  
    code.write(req.content) 
