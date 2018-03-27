import requests
from lxml import etree
import xlwt
from channel_infos import urls

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36','Connection':'keep-alive'}

def get_infos(url,number):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('Sheet1')
    header = ['title', 'author', 'public', 'time', 'price', 'score', 'comments', 'content', 'url']
    for h in range(0,len(header)):
        sheet.write(0, h, header[h])
    page_url = '{}?start={}&type=T'.format(url, number)
    print(page_url)
    html = requests.get(page_url, headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//li[@class="subject-item"]/div[2]')
    all_datas = []
    try:
        for info in infos:
            if info.xpath('h2/a/span/text()'):
                title = info.xpath('h2/a/@title')[0] + info.xpath('h2/a/span/text()')[0]
            else:
                title = info.xpath('h2/a/@title')[0]
            print(title)
            infomation = info.xpath('div[1]/text()')[0].strip().split('/')
            print(info)
            author = infomation[0]
            public = infomation[-3]
            time = infomation[-2]
            price = infomation[-1]
            score = info.xpath('div[2]/span[2]/text()')[0]
            comments = info.xpath('div[2]/span[3]/text()')[0].strip()
            contents = info.xpath('p/text()')[0]
            url = info.xpath('h2/a/@href')[0]
            data = [title, author, public, time, price, score, comments, contents, url]
            all_datas.append(data)
    except IndexError:
        pass
    i = 1
    for data in all_datas:
        j = 0
        for detail in data:
            sheet.write(i, j, detail)
            j = j + 1
        i = i + 1
    book.save('doubanbook.xls')


def get_all_links(url):
    for number in range(0, 20, 20):
        get_infos(url, number)


if __name__=="__main__":
    pool = Pool(processes=4)
    get_urls(start_url)
    pool.map(get_all_links, urls)

