import json
import requests
import jsonpath
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
urls = ['https://www.maizuo.com/api/film?__t=1522389699522&page={}&count=5&sortType=1&type=1'.format(i)for i in range(1, 5)]
for url in urls:
    time.sleep(3)
    res = requests.get(url, headers=headers)
    selector = res.text
    json_dict = json.loads(selector)
    try:
        for i in range(0, 5):
            name = jsonpath.jsonpath(json_dict, '$..films[%d].name'%i)[0]
            actors1 = jsonpath.jsonpath(json_dict, '$..films[%d].actors..name' %i)[0]
            actors2 = jsonpath.jsonpath(json_dict, '$..films[%d].actors..name' % i)[1]
            actors = actors1+actors2
            director = jsonpath.jsonpath(json_dict, '$..films[%d].director' % i)[0]
            category = jsonpath.jsonpath(json_dict, '$..films[%d].category' % i)[0]
            intro = jsonpath.jsonpath(json_dict, '$..films[%d].intro' % i )[0]
            print(name, actors, director, category, intro)
    except:
        pass


