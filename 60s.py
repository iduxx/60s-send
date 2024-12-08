import requests
import json
import time
import sys
import os
# -*- coding: utf-8 -*-

appToken = "AT_XXXXXXXX"
# 这里填你在WXpusher申请的apptoken


def get60s():
    url = "https://api.03c3.cn/api/zb"

    params = {
        "type":"jsonImg"
    }
    response = requests.get(url,params).json()
    return response["data"]['imageurl']
def gethtml(name,img_url):
    url = '"'+img_url+'"'
    ht = "<h1>"+name+",早上好"+"</h1><img src="+url+" alt="">"
    return ht
def send(dtt,img_url):
    tp = dtt.split("#")
    id = tp[0]
    name = tp[1]

    ht = gethtml(name,img_url)
    url = 'https://wxpusher.zjiecode.com/api/send/message'

    data = {
        "appToken": appToken,
        "content": ht,
        "summary": "60s",
        "contentType": 2,
        "uids": [id],
        "url": "http://dududududu.cn:327/",
        "verifyPay": 'false',
        "verifyPayType": 0
    }

    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post(url,data=json.dumps(data),headers=headers).json()
    # print(response)
    if response['code']==1000:
        return 1
    else :
        return response

if __name__ == '__main__':
    f = "False"
    dt = os.environ.get('ddd_dt', f)
    img_url = get60s()
    if dt == f:
        print("你没填变量啊刁毛 ddd_dt 格式：uid1#用户名1@uid2#用户名2")
        sys.exit()
    else:
        dt_run = dt.split('@')
        print(f'共获取到{len(dt_run)}个待发用户')
        i = 1
        print(f"60s--day\n")
        for dtt in dt_run:
            print(f'正在执行第{i}个用户')
            rp = send(dtt,img_url)
            if rp==1:
                print("successful  send!")
            else :
                print(rp)
            i = i + 1
    print(f"执行结束")