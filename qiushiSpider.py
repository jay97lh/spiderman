import requests
from lxml import etree

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

urls = 'https://www.qiushibaike.com/text/'
res = requests.get(urls)
selector = etree.HTML(res.text)
url_infos = selector.xpath('//div[@class="article block untagged mb15 typs_hot"]')
for url_info in url_infos:
	id = url_info.xpath('div[1]/a[2]/h2/text()')
print(id)