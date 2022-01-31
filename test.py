import pandas as pd
import bili_info as bInfo
import os

download = 'data\\'

if not os.path.exists(download):
    os.makedirs(download)

beg = 540192691
cnt = 0
res = 0
d = [[] for i in range(7)]
col = ['av', 'bv', 'title', 'view', 'danmushu', 'favorite', 'coin', 'share', 'like']

if os.path.exists(download + 'data.csv'):
    data = pd.read_csv(download + 'data.csv', encoding='utf-8')
    data = data[col]
else:
    data = pd.DataFrame(columns=col)

while res != 10000:
    c = bInfo.infoResolution(beg + cnt)
    if c is not None:
        print("AV{}\t爬取成功".format(beg + cnt), end="\t")
        c = [beg + cnt] + c
        print(c)
        c = pd.DataFrame(columns=col, data=[c])
        data = pd.concat([data, c])
        res += 1
    else:
        print("AV{}\t不存在".format(beg + cnt))
    cnt += 1

    if res % 100 == 0:
        print("当前爬取数量为\t{}".format(res))
        data.to_csv(download + "data.csv", encoding='utf-8', index=False)

data.to_csv(download + "data.csv", encoding='utf-8', index=False)
