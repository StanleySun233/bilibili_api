import json
import requests
import bs4
import bili_proxy as bProxy
import bili_danmu as bDanmu
import bili_id as bId
import datetime
import pandas as pd


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


def infoResolution(aid, isProxy=False):
    try:
        isP = isProxy
        bid = bId.av2bv(aid, isProxy=isP)
        info = getInfoMain(bid, isProxy=isP)
        cid = info['cid']
        title = info['title']
        stat = info['stat']
        view = stat['view']
        danmaku = stat['danmaku']
        fav = stat['favorite']
        coin = stat['coin']
        share = stat['share']
        like = stat['like']

        danmu = bDanmu.getBarrage(cid, isProxy=isP)

        if len(danmu) >= 5:
            f = open("data\\danmu\\av" + str(aid) + ".txt", 'w')
            for i in danmu:
                f.writelines(i + '\n')
            f.close()

        return [title, view, danmaku, fav, coin, share, like]
    except:
        return None


def getMainPage(isProxy=False):
    proxies, headers = bProxy.getHead(isProxy=isProxy)
    api = 'https://api.bilibili.com/x/web-interface/ranking/region?rid=1&day=3&original=0'

    if isProxy:
        a = requests.get(api, proxies=proxies, headers=headers)
    else:
        a = requests.get(api, headers=headers)
    a = a.text
    a = json.loads(a)['data']
    yy = datetime.datetime.now().year
    mm = datetime.datetime.now().month
    dd = datetime.datetime.now().day
    index = ['aid', 'bvid', 'typename', 'title', 'subtitle', 'play', 'review', 'video_review', 'favorites', 'mid',
             'author',
             'description', 'create', 'pic', 'coins', 'duration', 'badgepay', 'pts', 'redirect_url']
    t = []

    for i in a:
        temp = []
        for j in index:
            temp.append(i[j])
        t.append(temp)

    data = pd.DataFrame(columns=index, data=t)
    return [data, '{}-{}-{}'.format(yy, mm, dd)]
