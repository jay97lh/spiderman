import requests
from lxml import etree
import time
import pymongo

clinet = pymongo.MongoClient('localhost',27017)
mydb = clinet['mydb']
tongcheng_url = mydb['tongcheng_url']
tongcheng_info = mydb['tongcheng_info']
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36','Connection':'keep-alive'}

def get_links(channel, pages):
        list_view = '{}pn{}/'.format(channel, str(pages))
        html = requests.get(list_view,headers = headers)
        selector = etree.HTML(html.text)
        infos = selector.xpath('//div[@class="infocon"]/table/tbody/tr')
        for info in infos:
            url = info.xpath('td[2]/a/@href')[0]
            print(url)
            get_info(url)
            tongcheng_info.insert_one({'url':url})


def get_info(url):
        html = requests.get(url,headers=headers)
        selector = etree.HTML(html.text)
        try:
            title = selector.xpath('//h1/text()')[0]
            print(title)
            if selector.xpath('//span[@class="price_now"]/i/text()'):
                price = selector.xpath('//span[@class="price_now"]/i/text()')[0]
            else :
                price = '无'
            if selector.xpath('//div[@class="palce_li"]/span/i/text()'):
                area = selector.xpath('//div[@class="palce_li"]/span/i/text()')[0]
            else:
                area = '无'
            views = selector.xpath('//p[@class="info_p"]/span[1]/text()')[0]
            wants = selector.xpath('//span[@class="want_person"]/text()')[0]
            info = {
                'title':title,
                'price':price,
                'area':area,
                'views':views,
                'wants':wants,
                'url':url
            }
            tongcheng_info.insert_one(info)
        except IndexError:
            pass



