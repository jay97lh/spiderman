import requests
from lxml import etree
import re
import pymongo

client = pymongo.MongoClient('localhost',27017)
mydb = client['mydb']
musictop = mydb['MusicTop']

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

def get_url_music (url):
	html = requests.get(url,headers=headers)
	selector = etree.HTML(html.text)
	music_hrefs = selector.xpath('//a[@class="nbg"]/@href')
	for music_href in music_hrefs:
		get_music_info(music_href)
		
def get_music_info(url):
	html = requests.get(url,headers=headers)
	selector =etree.HTML(html.text)
	name = selector.xpath('//div[@id="wrapper"]/h1/span/text()')[0]
	author = selector.xpath('//*[@id="info"]/span/span/a/text()')[0]
	style = re.findall('<span class="pl">流派:</span>&nbsp;[\u4e00-\u9fa5][\u4e00-\u9fa5]<br>',html.text,re.S)
	if len(style)==0:
		style = "未知"
	else:
		style = style[0].strip()
	time = re.findall('<span class="pl">发行时间:</span>&nbsp;(.*?){12}<br>',html.text,re.S)[0].strip()
	if len(publishers)==0:
		publishers = '未知'
	else :
		publishers = publishers[0].strip()
	score = selector.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')[0]
	print (name,author,style,time,publishers,score)
	info = {
			'name':name,
			'author':author,
			'style':style,
			'time':time,
			'publisher':publishers,
			'score':score
			}
	musictop.insert_one(info)
	
	

if __name__=="__main__":
		urls = ['https://music.douban.com/top250?start={}'.format(str(i))for i in range(0,250,25)]
		for url in urls:
			get_url_music(url)
