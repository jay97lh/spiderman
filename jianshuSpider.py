import requests
import pymongo
from lxml import etree
from multiprocessing import Pool

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
clinet = pymongo.MongoClient('localhost',27017)
mydb = clinet['mydb']
jianshu_shouye = mydb['jianshu_shouye']

def get_jianshu_info(url):
        html = requests.get(url,headers=headers)
        selector = etree.HTML(html.text)
        infos = selector.xpath('//div[@id="list-container"]/ul/li')
        for info in infos:
                try:
                    author = info.xpath('div/div[1]/div/a/text()')[0]
                    title = info.xpath('div/a/text()')[0]
                    time = info.xpath('div/div[1]/div/span/@data-shared-at')[0]
                    comtent = info.xpath('div/p/text()')[0].strip()
                    comments = info.xpath('div/div[2]/a[2]/text()')[1].strip()
                    views = info.xpath('div/div[2]/a[1]/text()')[1].strip()
                    data = {
                            'author':author,
                            'title':title,
                            'time':time,
                            'comtent':comtent,
                            'comments':comments,
                            'views':views
                    }
                    jianshu_shouye.insert_one(data)
                except IndexError:
                    pass

if __name__=="__main__":
    urls = ['https://www.jianshu.com/c/bDHhpK?order_by=commented_at&page={}'.format(i)for i in range(1,20)]
    pool= Pool(processes=4)
    pool.map(get_jianshu_info,urls)