import requests
import pymongo
import csv
import time
from selenium import webdriver

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
qzone = mydb['qzone']

driver = webdriver.Chrome()
driver.maximize_window()

def get_info(qq):
    try:
        driver.get('https://user.qzone.qq.com/{}/311'.format(qq))
    except WebDriverException:
        qzone.insert_one(qq)
        print('{}get a English Emai'.format(qq))
    try:
        driver.find_element_by_id('login_div')
        a = True
    except:
        a = False
    if a == True:
        driver.switch_to.frame('login_frame')
        try:
            driver.find_element_by_id('switcher_plogin').click()
            driver.find_element_by_id('u').clear()
            driver.find_element_by_id('u').send_keys('')
            driver.find_element_by_id('p').clear()
            driver.find_element_by_id('p').send_keys('')
            driver.find_element_by_id('login_button').click()
            time.sleep(5)
        except:
            driver.find_element_by_id('u').clear()
            driver.find_element_by_id('u').send_keys('')
            driver.find_element_by_id('p').clear()
            driver.find_element_by_id('p').send_keys('')
            driver.find_element_by_id('login_button').click()
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_id('QM_OwnerInfo_ModifyIcon')
        b = True
    except:
        b = False
    if b == True:
        driver.switch_to.frame('app_canvas_frame')
        contents = driver.find_element_by_css_selector('.content')
        times = driver.find_element_by_css_selector('.c_tx.c_tx4.goDetail')
        for content, tim in zip(contents, times):
            data = {
                'content':content,
                'time':tim
            }
            qzone.insert_one(data)

if __name__=="__main__":
    qq_lists = []
    fp = open('D:\Download\QQMail.csv')
    reader = csv.DictReader(fp)
    for row in reader:
        qq_lists.append(row['电子邮件'].split('@')[0])
    fp.close()
    for item in qq_lists:
        get_info(item)