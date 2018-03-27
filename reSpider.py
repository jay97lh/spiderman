import requests
import re

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

info_lists = []

def jugement_sex(class_name):
	if class_name == manIcon:
		return 'Man'
	else:
		return 'Womam'
		
def get_info(url):
	wb_data = requests.get(url)
	ids = re.findall('<h2>(.*?)</h2>',wb_data.text,re.S)
	levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>',wb_data.text,re.S)
	sexs = re.findall('<div class="articleGender (.*?)">\D+</div>',wb_data.text,re.S)
	contents = re.findall('<div class="content">.*?<span>(.*?)</span></div>',wb_data.text,re.S)
	laughs = re.findall('<span class="stats-vote"><i class="number">(.*?)</i> .*?</span>',wb_data.text,re.S)
	comments =re.findall('<i class="number">(\d+)</i>',wb_data.text,re.S)
	for id,level,laugh,comment in zip(ids, levels, laughs, comments):
		info = {
				'id':id,
				'level':level,
				#'sex':jugement_sex(sexs),
				#'content':content,
				'laugh':laugh,
				'comment':comment
			}
		print (info)
		info_lists.append(info)
		
		
if __name__=="__main__":
	urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i))for i in range(1,4)]
	for url in urls:
		get_info(url)
	for info_list in info_lists:
		f = open('D:/GoodGoodStudy/Spider/text/qiushi.text','a+')
		try:
			f.write(info_list['id']+'\n')
			f.write(info_list['level']+'\n')
			#f.write(info_list['sex']+'\n')
			#f.write(info_list['content']+'\n')
			f.write(info_list['laugh']+'\n')
			f.write(info_list['comment']+'\n')
			f.close()
		except UnicodeEncodeError:
			pass
			