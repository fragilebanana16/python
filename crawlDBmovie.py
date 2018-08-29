import os,time
import requests
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.error import HTTPError
from bs4 import BeautifulSoup
#这里DUMMY意味着多线程而不是多进程
from multiprocessing.dummy import Pool
import multiprocessing
import re
#豆瓣电影每25个一页，发现url切换页面的规律只有start=有递增25
url2 = ["http://www.mmjpg.com/home/{}".format(i) for i in range(1,40)]
urls = ["https://movie.douban.com/top250?start={}&filter=".format(i) for i in range(0,50,25)]
def fun(url):
    print("ok") 
    #安全处理
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("Title could not be found")

    if html == None:
        print("Title could not be found")
    else:
        pass
    #创建bs对象
    bs = BeautifulSoup(html.read(),features="html.parser")
    #分析网页源码结构
    movieList=bs.find('ol',attrs={'class':'grid_view'})
    #存储提取信息
    names = []
    ratings = []
    imgs = []
    #bs.find属性
    for tagLi in movieList.findAll('li'):
        nameList = tagLi.find("div", {"class":"hd"})
        movieName = nameList.find('span',{'class':'title'}).getText()
        ratingList = tagLi.find("div", {"class":"star"})
        rating = ratingList.find('span',{"class":"rating_num"}).getText()
        img = tagLi.find("img",{"width":"100"})
        imgs.append(img.attrs['src'])
        names.append(movieName)
        ratings.append(rating)
    #创建文件夹
    os.makedirs('./img/',exist_ok=True)
    #打印提取信息
    for (name,rating,img) in zip(names,ratings,imgs):
        print(name)
        print(rating)
        print(img)
        r = requests.get(img,stream=True)
        #格式命名文件
        imageName = '['+rating+']'+name+'.png'
        #下载图片
        with open('./img/%s' % imageName,'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('saved %s'% imageName)
def get_url(url):
    html = requests.get(url)
    #print(html.url)

##time1 = time.time()
##for url in urls:
##    fun(url)
##time2 = time.time()
##print('1线程耗时' + str(time2 - time1))
    
pool = Pool(4)
time3 = time.time()
results = pool.map(fun, urls)
pool.close()
pool.join()
time4 = time.time()
print('多线程耗时' + str(time4 - time3))


       
   
    
