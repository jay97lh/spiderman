from lxml import etree
import requests
import xlwt

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

all_info_list=[]

def get_info(url):
	html = requests.get(url,headers = headers)
	selector = etree.HTML(html.text)
	infos = selector.xpath('//div[@class="product item-1111 "]/div')
	for info in infos :
		name1 = info.xpath('div[2]/a[1]/span/text()')[0]
		name2 = info.xpath('div[2]/a[1]/text()')[0].strip('/')
		name3 = info.xpath('div[2]/a[2]/text()')[0]
		name = name1+name2+name3
		price = info.xpath('p[1]/em/text()')[0]
		url = info.xpath('div[2]/a[1]/@href')[0]
		info_list = [name,price,url]
		all_info_list.append(info_list)
		
if __name__=="__main__":
	url = 'https://list.tmall.com/search_product.htm?q=mac%BF%DA%BA%EC&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton'
	get_info(url)
	
	header = ['name','price','url']
	
	book = xlwt.Workbook(encoding='utf-8')
	sheet = book.add_sheet('Sheet1')
	for h in range(len(header)):
		sheet.write(0,h,header[h])
	i = 1
	for list in all_info_list:
		j = 0
		for data in list:
			sheet.write(i,j,data)
			j = j+1
		i = i+1
book.save('Mac.xls')		