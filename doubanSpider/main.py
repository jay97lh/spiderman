import sys
sys.path.append("..")
from channel_infos import urls
from channel_infos import get_urls
from page_spider import get_infos
from multiprocessing import Pool
start_url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-hot#%E6%96%87%E5%AD%A6'

def get_all_links(url):
    for number in range(0, 20, 20):
        get_infos(url, number)

if __name__ == "__main__":
    pool = Pool(processes=8)
    get_urls(start_url)
    pool.map(get_all_links, urls)

