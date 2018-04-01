from lxml import etree
import requests
import time
import random

ip_list = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
urls = ['http://www.xicidaili.com/nn/{}'.format(i)for i in range(1, 5)]
def get_ip_list(url):
    time.sleep(3)
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//tr')
    info_list = infos[1:]
    for info in info_list:
         ip = info.xpath('td[2]/text()')[0]
         ip_list.append(ip)

def get_proxies_list(ip_list):
    proxies_list = []
    for ip in ip_list:
        proxie_ip = 'http://'+ip
        proxies_list.append(proxie_ip)
    proxy_ip = random.choice(proxies_list)
    proxies = {'http': proxy_ip}
    return proxies


#res = requests.get(url,headers,proxies=proxies)
