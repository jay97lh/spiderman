import json
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
lagou = mydb['lagou']

headers = {'Cookie':'！！！',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Sa',
            'Connection':'keep-alive'
            }
def get_page(url, params):
    html = requests.post(url, data=params, headers=headers)
    print(html.text)
    json_data = json.loads(html.text)
    total_count = json_data['content']['positionResult']['totalCount']
    page_number = int(total_count/15)if int(total_count/15)<30 else 30
    get_info(url,page_number)

def get_info(url, page):
    for pn in range(1,page+1):
        time.sleep(3)
        params = {
            'first': 'true',
            'pn': str(pn),
            'kd': 'python'
        }
        try:
            html = requests.post(url, data=params, headers=headers)
            json_data = json.loads(html.text)
            results = json_data['content']['result']
            for result in results:
                infos = {
                    'companyFullName':result['companyFullName'],
                    'city':result['city'],
                    'businessZones':result['businessZones'],
                    'companyId':result['companyId'],
                    'companyLabelList':result['companyLabelList']
                }
                lagou.insert_one(infos)
        except requests.exceptions.ConnectionError:
            pass

if __name__=="__main__":
    url = "https://www.lagou.com/jobs/positionAjax.json"
    params = {
        'first': 'true',
        'pn': '1',
        'kd': 'python'
    }
    get_page(url,params)