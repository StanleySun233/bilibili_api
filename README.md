# b站公开API接口的调用
# 作者：Stanley Sun
# 已实现功能

## 1. [proxy](bili_proxy.py)
设置代理。

### 1.1 [Uesr-Agent](bili_proxy.py)
本项目默认提供100个User-Agent，无需设置。
```
def getRandomUA(path='2021-100-PC.txt')
```

### 1.2 [代理](bili_proxy.py)
建议首先设置代理。
```
getHead(isProxy=False, delayTime=0.2, proxyHost=None, proxyPort=None, proxyUser=None, proxyPass=None)
```

## 2. [danmu](bili_danmu.py)
调用接口解析弹幕。

### 2.1 [弹幕](bili_danmu.py)
通过cid读取弹幕，解析为txt文本。
```
getBarrage(cid, isProxy=False)
```

## 3. [id](bili_id.py)
提供av号、bv号、cv号的转换。

### 3.1 [av号转bv号](bili_id.py)
通过访问视频主站提取bv号。
```
av2bv(aid, isProxy=False)
```

### 3.2 [bv号转av号](bili_id.py)
通过调用接口获取json字典，解析为dict结构，提取av号。
```
bv2av(bid, isProxy=False)
```

### 3.3 [bv号转cv号](bili_id.py)
通过调用接口获取json字典，解析为dict结构，提取cv号。
```
bv2cv(bid, isProxy=False)
```

## 4. [info](bili_info.py)
各种关于视频信息的接口转化为本地数据。

### 4.1 [解析主要数据](bili_info.py)
解析为json后提取键data。
```
def getInfoMain(bid, isProxy=False)
```

### 4.2 [解析全部数据](bili_info.py)
解析为json后返回所有信息。
```
def getInfoAll(bid, isProxy=False)
```

### 4.3 [当天首页推荐](bili_info.py)
获取首页推荐，返回DataFrame和date。
```
def getMainPage(isProxy=False)
```

### 4.4 [处理数据](bili_info.py)
将json数据解析为list格式，并保存弹幕。
```
def infoResolution(aid,isProxy = False)
```
