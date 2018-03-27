import requests
import csv
from lxml import etree

fp = open('D:/GoodGoodStudy/Spider/text/doubanbook.csv','wt',newline='',encoding = 'utf-8')
writer = csv.writer(fp)
writer.writerow(('name','url','author','publisher','date','price','rate','comment'))

urls = ['https://book.douban.com/top250?start={}'.format(str(i))for i in range(0,100,25)]

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

for url in urls:
	html = requests.get(url,headers=headers)
	selector = etree.HTML(html.text)
	infos = selector.xpath('//tr[@class="item"]')
	for info in infos:
		name = info.xpath('td/div/a/@title')[0]
		url = info.xpath('td/div/a/@href')[0]
		book_info = info.xpath('td/p/text()')[0]
		author = book_info.split('/')[0]
		publisher = book_info.split('/')[-3]
		date = book_info.split('/')[-2]
		price = book_info.split('/')[-1]
		rate = info.xpath('td/div/span[2]/text()')[0]
		comments = info.xpath('td/p/span/text()')
		comment = comments[0] 
		writer.writerow((name,url,author,publisher,date,price,rate,comment))

fp.close()
		
		
