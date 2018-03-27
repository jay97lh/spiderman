import requests
from lxml import etree

url = 'https://book.douban.com/tag/%E7%A7%91%E6%8A%80?start=0&type=T'

def get_info(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//li[@class="subject-item"]/div[2]')
    for info in infos:
        if info.xpath('h2/a/span/text()'):
            name = info.xpath('h2/a/@title')[0]+info.xpath('h2/a/span/text()')[0]
        else:
            name = info.xpath('h2/a/@title')[0]
        print(name)
        infomation = info.xpath('div[1]/text()')[0].strip().split('/')
        print(infomation)
        score = info.xpath('div[2]/span[2]/text()')[0]
        print(score)
        comments = info.xpath('div[2]/span[3]/text()')[0].strip()
        print(comments)
        contents = info.xpath('p/text()')[0]
        print(contents)

get_info(url)