import bs4
import requests
import bili_proxy as bProxy


def getBarrage(cid, isProxies=False):
    proxies, headers = bProxy.getHead()
    api = 'https://api.bilibili.com/x/v1/dm/list.so?oid=' + str(cid)
    res = []

    if isProxies:
        r = requests.get(api, proxies=proxies, headers=headers)
    else:
        r = requests.get(api, headers=headers)
    r = r.content.decode(encoding='utf-8')
    bs = bs4.BeautifulSoup(r, 'xml')
    t = bs.find_all(["d"])
    for i in t:
        res.append(str(i.string))
    return res
