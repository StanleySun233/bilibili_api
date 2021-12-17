import requests
import bs4
import json
import bili_proxy as bProxy
import bili_info as bInfo


def av2bv(aid, isProxy=False):
    api = 'https://www.bilibili.com/video/av' + str(aid)

    proxies, headers = bProxy.getHead(isProxy=isProxy)
    if isProxy:
        a = requests.get(api, proxies=proxies, headers=headers)
    else:
        a = requests.get(api, headers=headers)

    a = bs4.BeautifulSoup(a.content.decode('utf-8'), 'lxml')
    a = a.find_all('meta')
    res = None
    for i in range(len(a)):
        if 'BV' in str(a[i]):
            b = str(a[i])
            z1 = b.index('BV')
            z2 = b[z1:].index('/')
            res = b[z1 + 2:z1 + z2]
            break
    return res


def bv2av(bid, isProxy=False):
    proxies, headers = bProxy.getHead(isProxy=isProxy)
    api = 'https://api.bilibili.com/x/web-interface/view?bvid=' + bid

    if isProxy:
        a = requests.get(api, proxies=proxies, headers=headers)
    else:
        a = requests.get(api, headers=headers)

    bs = bs4.BeautifulSoup(a.text, 'lxml')
    bs = str(bs.p.string)
    info = json.loads(bs)
    info = dict(info)
    return info['data']['aid']


def bv2cv(bid, isProxy=False):
    info = bInfo.getInfoMain(bid, isProxy=isProxy)
    return info['cid']
