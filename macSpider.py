from lxml import etree
import csv
import requests

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

res = requests.get('https://s.taobao.com/search?q=mac%E5%8F%A3%E7%BA%A2&imgfile=&js=1&stats_click=search_radio_tmall%3A1&initiative_id=staobaoz_20180308&tab=mall&ie=utf8',headers = headers)
print (res.text)
fp = open('D:/GoodGoodStudy/Spider/text/mac.csv','wt',newline = '',encoding = 'utf-8')
writer = csv.writer(fp)
writer.writerow(('name','price','url'))

selector = etree.HTML(res.text)
infos = selector.xpath('//div[@class="ctx-box J_MouseEneterLeave J_IconMoreNew"]')
print (infos)

for info in infos:
	name = info.xpath('//*[@id="J_Itemlist_TLink_546724870335"]/text()')
	print (name)