import requests
from lxml import etree
from multiprocessing import Pool
import xlwt
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Connection': 'keep-alive'}
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
            urls.append(url_host + channel_url)


def get_infos(url, number):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('Sheet1')
    header = ['title', 'author', 'public', 'time', 'price', 'score', 'comments', 'content', 'url']
    for h in range(0, len(header)):
        sheet.write(0, h, header[h])
    page_url = '{}?start={}&type=T'.format(url, number)
    print(page_url)
    html = requests.get(page_url, headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//li[@class="subject-item"]/div[2]')
    all_datas = []
    try:
        for info in infos:
            time.sleep(20)
            if info.xpath('h2/a/span/text()'):
                title = info.xpath('h2/a/@title')[0] + info.xpath('h2/a/span/text()')[0]
            else:
                title = info.xpath('h2/a/@title')[0]
            infomation = info.xpath('div[1]/text()')[0].strip().split('/')
            author = infomation[0]
            public = infomation[-3]
            date = infomation[-2]
            price = infomation[-1]
            score = info.xpath('div[2]/span[2]/text()')[0]
            comments = info.xpath('div[2]/span[3]/text()')[0].strip()
            contents = info.xpath('p/text()')[0]
            url = info.xpath('h2/a/@href')[0]
            data = [title, author, public, date, price, score, comments, contents, url]
            print(data)
            all_datas.append(data)
    except IndexError:
        pass

    i = 1
    for data in all_datas:
        j = 0
        for detail in data:
            sheet.write(i, j, detail)
            j = j+1
        i = i + 1
    book.save('doubanbook.xls')


def get_all_links(url):
    for number in range(0, 20, 20):
        get_infos(url, number)


if __name__ == "__main__":
    pool = Pool(processes=8)
    get_urls(start_url)
    pool.map(get_all_links, urls)
