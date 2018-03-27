import requests
from lxml import etree

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

def get_info(url):
    res = requests.get(url,headers=headers)
    selector = etree.HTML(res.text)
    infos = selector.xpath('//div[@class="infocon"]/table/tbody/tr')
    for info in infos:
        url = info.xpath('td[2]/a/@href')[0]
        print(url)

if __name__=='__main__':
        url = 'http://hf.58.com/sanxing/pn1/'
        get_info(url)