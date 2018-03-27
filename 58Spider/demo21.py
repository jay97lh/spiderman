import requests
from lxml import etree

headers =  {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36','Connection':'keep-alive'}
def get_info(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    title = selector.xpath('//h1/text()')[0]
    print(title)
    price = selector.xpath('//span[@class="price_now"]/i/text()')[0]
    print(price)
    area = selector.xpath('//div[@class="palce_li"]/span/i/text()')[0]
    print(area)
    views = selector.xpath('//p[@class="info_p"]/span[1]/text()')[0]
    print(views)
    wants = selector.xpath('//span[@class="want_person"]/text()')[0]
    print(wants)
    info = {
            'title': title,
            'price': price,
            'area': area,
            'views': views,
            'wants': wants,
            'url': url
        }


if __name__=="__main__":
    url = 'http://zhuanzhuan.58.com/detail/971918502704070663z.shtml?fullCate=5%2C36%2C487&amp;fullLocal=837&amp;from=pc&amp;metric=null'
    get_info(url)