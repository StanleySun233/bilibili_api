import pandas as pd
import bili_info as bInfo
import os

ospath = 'data\\'

if not os.path.exists(ospath):
    os.makedirs(ospath)

beg = 540192691
cnt = 0
res = 0
d = [[] for i in range(7)]
col = ['av', 'title', 'view', 'danmushu', 'favorite', 'coin', 'share', 'like']
if os.path.exists(ospath + 'data.csv'):
    data = pd.read_csv(ospath + 'data.csv', encoding='utf-8')
else:
    data = pd.DataFrame(columns=col)

while res != 10000:
    c = bInfo.infoResolution(beg + cnt)
    if c is not None:
        print("AV{}\t爬取成功".format(beg+cnt))
        print(c)
        c = [beg + cnt] + c
        c = pd.DataFrame(columns=col, data=[c])
        data = pd.concat([data, c])
        res += 1
    else:
        print("AV{}\t不存在".format(beg+cnt))
    cnt += 1
    print("当前爬取数量为\t{}".format(res))
    if res % 100 == 0:
        data.to_csv(ospath + "data.csv")

data.to_csv(ospath + "data.csv", encodings='utf-8')
