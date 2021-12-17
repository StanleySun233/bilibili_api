# b站公开API接口的调用

# 已实现功能
## 1.[弹幕](bili_danmu.py)
```
getBarrage(cid, isProxies=False) # 需要获取cid，可以自定义代理。
```

## 2.[av号转bv号](bili_id.py)
```
av2bv(aid, isProxy=False) # 通过访问网站提取bv号，可以自定义代理。
```

## 3.[bv号转av号](bili_id.py)
```
bv2av(bid, isProxy=False) # 通过调用接口获取json字典，解析为dict结构，提取av号，可以自定义代理。
```

## 4.[bv号转cv号](bili_id.py)
```
bv2cv(bid, isProxy=False) # 通过调用接口获取json字典，解析为dict结构，提取cv号，可以自定义代理。
```