# 网络图片爬取和存储

import requests
import os
root = '/home/liushiyuan/'
url ='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1542082788505&di=e726e96dcc25abce795505d6f5f49d7c&imgtype=0&src=http%3A%2F%2Fe.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2F562c11dfa9ec8a13aff433b3fa03918fa1ecc0f3.jpg'
path = root+url.split('/')[-1]
r = requests.get(url)
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r =requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('save file')
    else:
        print('save error')
except:
    print('爬取失败')