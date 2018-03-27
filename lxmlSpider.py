import requests
from bs4 import BeautifulSoup
import re
from lxml import etree

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

def get_info(url):
	wb_data = requests.get(url,headers)
	print (wb_data.text)
	soup = BeautifulSoup(wb_data.text,'lxml')
	titles = soup.select('#plist > ul > li > div > div.p-name > a > em') 
	imgs = soup.select('#plist > ul > li > div > div.p-img > a > img')
	prices = re.findall('<strong class="J_price"><em>¥</em><i>(.*?)</i></strong>',wb_data.text,re.S)
	print(prices)
	for title,img,price in zip(titles,imgs,prices):
		data = {
				'title':title.get_text().strip(),
				'price':price,
				'img':img.get('src')
				}
		
if __name__=="__main__":
	urls = ['https://list.jd.com/list.html?cat=9987,653,655&page={}&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'.format(str(i))for i in range(1,3)]
	for url in urls :
		get_info(url)