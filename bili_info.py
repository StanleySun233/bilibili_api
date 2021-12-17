import json
import requests
import bs4
import bili_proxy as bProxy
import bili_danmu as bDanmu
import bili_id as bId


def getInfoMain(bid, isProxy=False):
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
    data = info['data']
    return data


def getInfoAll(bid, isProxy=False):
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
    return info


def infoResolution(aid):
    try:
        bid = bId.av2bv(aid)
        info = getInfoMain(bid)
        cid = info['cid']
        title = info['title']
        stat = info['stat']
        view = stat['view']
        danmaku = stat['danmaku']
        fav = stat['favorite']
        coin = stat['coin']
        share = stat['share']
        like = stat['like']

        danmu = bDanmu.getBarrage(cid)

        if len(danmu) >= 5:
            f = open("data\\danmu\\av" + str(aid) + ".txt", 'w')
            for i in danmu:
                f.writelines(i + '\n')
            f.close()

        return [title, view, danmaku, fav, coin, share, like]
    except:
        return None