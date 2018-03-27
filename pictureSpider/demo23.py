from bs4 import BeautifulSoup
from lxml import etree
import requests
import time

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

urls = ['https://www.pexels.com/search/book/?page={}'.format(i)for i in range(2,5)]
list = []
for url in urls :
    time.sleep(3)
    wb_data = requests.get(url, headers=header)
    infos = etree.HTML(wb_data.text)
    imgs = infos.xpath('//div[@class="photos"]/article/a')
    for img in imgs :
        src = img.xpath('img/@data-large-src')[0]
        print(src)
        list.append(src)
path = r'C:/Users/Jay/Pictures/demo/'
i = 1
for item in list:
    data = requests.get(item, headers=header)
    fp = open(path+str(i)+'.jpg', 'wb')
    fp.write(data.content)
    fp.close()
    print('get'+str(i))
    i = i+1