import random
import time


def getRandomUA(path='2021-100-PC.txt'):
    f = open(path, 'r')
    UA = f.readlines()
    index = random.randint(0, len(UA))
    return UA[index].replace("\n", "")


def getHead(isProxy=False, delayTime=0.2, proxyHost=None, proxyPort=None, proxyUser=None, proxyPass=None):
    time.sleep(delayTime)
    proxies = None
    if isProxy:
        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }

        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }

    tunnel = random.randint(1, 10000)
    headers = {"Proxy-Tunnel": str(tunnel),
               'User-Agent': getRandomUA()}
    return [proxies, headers]
