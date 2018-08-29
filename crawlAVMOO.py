import os
import requests
from urllib import request
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import re
count = 0
picUrl = []
nums = []
names = []
for page in range(1,3,1):
    url = "https://javmoo.com/cn/search/abp/page/"+str(page)
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(url, headers = head)
    response = request.urlopen(req)
    html = response.read()
    bs = BeautifulSoup(html,'lxml')
    movieList = bs.find_all('div',attrs={'class':'item'})
    for tagLi in movieList:
        count += 1
        picUrl.append(tagLi.img.attrs['src'])
        nums.append(tagLi.find('date').get_text())
        names.append(tagLi.img.attrs['title'])
    print(count)
    os.makedirs('./img/',exist_ok=True)
    for (name,img,num) in zip(names,picUrl,nums):
        r = requests.get(img,stream=True)
        imageName = '['+num+']'+name+'.png'
        with open('./img/%s' % imageName,'wb+') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('saved %s'% imageName)        
   
    
