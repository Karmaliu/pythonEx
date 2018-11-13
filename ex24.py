import requests
import re


def start_spider():
    r = requests.get('https://www.jianshu.com/p/d8a59076d031')
    pattern = '<h1>.*?</h1>'
    duanzi_list = re.findall(pattern, r.text, re.S)
    print(duanzi_list)


start_spider()
