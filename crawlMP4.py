import requests,time
from lxml import etree
from multiprocessing import Process
from multiprocessing.dummy import Pool
import multiprocessing
outterUrl = ["https://ibaotu.com/shipin/7-5023-0-0-1-{}.html".format(i) for i in range(1,2)]

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
#爬取短视频：首页收集外链，for循环再次请求查找视频src
def doit(url,title):  
    
    response = requests.get(url=url,headers=headers)
    html = response.content.decode()
    html = etree.HTML(html)       
    src = html.xpath('//div[@class="img-wrap"]/a[@class="video-src"]/@src')
    #print(type(src))
    s = "".join(src)
    write_file(s,title)
    #print(s)
def write_file(video_src, video_title):
    
    response = requests.get("http:"+ video_src, headers=headers)
    file_name = video_title + ".mp4"
    print("正在抓取%s" % file_name)
    with open(file_name, "wb") as f:
        f.write(response.content)
def start_work(outterUrl):
    response = requests.get(url=outterUrl,headers=headers)
    html = response.content.decode()
    html = etree.HTML(html)

    video_src = html.xpath('//div[@class="video-titbox"]/a/@href')
    video_title = html.xpath('//span[@class="video-title"]/text()')
    for s,t in zip(video_src,video_title):
        fullSrc = "http:" + s
        doit(fullSrc,t)
if __name__ == '__main__' :
    startTime = time.time()  
    #start_work(outterUrl)
    for url in outterUrl:
        start_work(url)
    

##    p=Pool(20)
##    p.map(start_work,outterUrl)
##    p.close()
##    p.join()
    endTime = time.time()
    print("%0.4f secs"%(endTime -startTime ))
    #write_file(s, "123")

   




