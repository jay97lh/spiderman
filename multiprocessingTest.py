import requests
import re 
import time
from multiprocessing import Pool

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

fp = open('D:/GoodGoodStudy/Spider/text/qiushi.txt','a+')

def re_scarper(url):
	res = requests.get(url,headers=headers)
	ids = re.findall('<h2>(.*?)</h2>',res.text,re.S)
	print(ids)
	contents = re.findall(' <div class="content"><span>(.*?)</span></div>',res.text,re.S)
	print(contents)
	laughs = re.findall('<div class="stats">.*?<span class="stats-vote"><i class="number">(\d+)</i>',res.text,re.S)
	print(laughs)
	comments = re.findall('<span class="stats-comments"><span class="dash">.*?<i class="number">(.*?)</i>',res.text,re.S)
	print(comments)
	for id,content,laugh,comment in zip(ids,contents,laughs,comments):
		info = {
				'id':id,
				'content':content,
				'laugh':laugh,
				'comment':comment
				}
		print(info)
		fp.write(info+'\n')
		return info
		
if __name__=="__main__":
	urls = ['https://www.qiushibaike.com/text/page/{}/'.format(i)for i in range(1,13)]
	start_1 = time.time()
	for url in urls:
		re_scarper(url)
	end_1 = time.time()
	print('串行爬虫：',end_1-start_1)
	start_2 = time.time()
	pool = Pool(processes=2)
	pool.map(re_scarper, urls)
	end_2 = time.time()
	print('两个进程：',end_2-start_2)
	start_3 = time.time()
	pool = Pool(processes=4)
	pool.map(re_scarper, urls)
	end_3 = time.time()
	print('四个进程：',end_3-start_3)

fp.close()