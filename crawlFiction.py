from urllib import request
from bs4 import BeautifulSoup
if __name__ == '__main__':
##    #单url爬取
##    url = 'http://www.136book.com/daomubijiqianchuan/qlxexecac/'
##    head = {}
##    # 使用代理
##    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
##    req = request.Request(url, headers = head)
##    response = request.urlopen(req)
##    html = response.read()
##    # 创建request对象
##    soup = BeautifulSoup(html, 'lxml')
##    # 找出div中的内容
##    soup_text = soup.find('div', id = 'content')
##    soup_p = soup_text.find_all("p")
##    # 输出其中的文本
##    for p in soup_p:
##        print("  "+p.get_text())
    # 目录页
    url = 'http://www.136book.com/daomubijiqianchuan/'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(url, headers = head)
    response = request.urlopen(req)
    html = response.read()
    f = open('daomubiji.txt','w+')
    # 解析目录页
    soup = BeautifulSoup(html, 'lxml')
    # find_next找到第二个<div>
    soup_texts = soup.find('div', id = 'book_detail', class_= 'box1').find_next('div')
    # 遍历ol的子节点，打印出章节标题和对应的链接地址
    for link in soup_texts.ol.children:
        if link != '\n':
            #print(link.text + ':', link.a.attrs['href'])
            #link.a.get('href') is also ok
            downUrl = link.a.attrs['href']
            downReq = request.Request(downUrl, headers = head)
            downResponse = request.urlopen(downReq)
            downHtml = downResponse.read()
            downSoup = BeautifulSoup(downHtml, 'lxml')
            soup_text = downSoup.find('div', id = 'content')
            soup_p = soup_text.find_all("p")
            # 写入章节标题
            f.write(link.text + '\n\n')
            # 写入章节内容
            for p in soup_p:
                f.write("  "+p.get_text())
            f.write('\n\n')
    f.close()
    print("done!")
            
            
