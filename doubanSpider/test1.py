import requests
from lxml import etree

url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-hot#%E6%96%87%E5%AD%A6'
url_host = 'https://book.douban.com'
headers = headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36','Connection':'keep-alive'}

def get_url(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//td')
    for info in infos:
        text = info.xpath('a/text()')[0]
        url = info.xpath('a/@href')[0]


if __name__=="__main__":
    get_url(url)