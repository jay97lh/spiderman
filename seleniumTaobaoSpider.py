from selenium import webdriver
from lxml import etree
import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
taobao = mydb['taobao']

driver = webdriver.Chrome()
driver.maximize_window()

def next_page(url,page):
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//a[@trace="srp_bottom_pagedown"]').click()
    time.sleep(3)
    driver.get(driver.current_url)
    get_info(driver.current_url, page)

def get_info(url, page):
    page = page+1
    driver.get(url)
    driver.implicitly_wait(10)
    selector = etree.HTML(driver.page_source)
    infos = selector.xpath('//div[@id="ctx-box J_MouseEneterLeave J_IconMoreNew"]')
    for info in infos:
        title = info.xpath('div/a/text()')[0].strip()
        print('title')
        price = info.xpath('div/div/strong/text()')[0]
        print('price')
        store = info.xpath('div/div/span[2]/text()')[0]
        print('store')
        data = {
            'title': title,
            'price': price,
            'store': store
        }
        taobao.insert_one(data)
    if page < 3:
        next_page(driver.current_url, page)
    else:
        pass

if __name__=="__main__":
    url = "http://www.taobao.com"
    driver.get(url)
    driver.find_element_by_id("q").clear()
    driver.find_element_by_id("q").send_keys("奥迪双钻")
    driver.find_element_by_class_name("btn-search").click()
    page = 1

get_info(driver.current_url ,page)
