import requests
from lxml import etree
import xlwt

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36', 'Connection':'keep-alive'}
url_host = 'https://book.douban.com'
start_url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-hot#%E6%96%87%E5%AD%A6'
urls = []

def get_urls(start_url):
    html = requests.get(start_url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//td')
    for info in infos:
        channel_url = info.xpath('a/@href')[0]
        if channel_url == 'https://ypy.douban.com':
            pass
        else:
            urls.append(url_host+channel_url)

