
# page_parser 包使用示例：6行代码写爬虫

import json
import requests
import datetime
from page_parser.weixin_parser import WeixinParser

# 1、下载网页
response = requests.get("https://mp.weixin.qq.com/s/fZp8gs-Uayckuia6WJ89ag")
html = response.content.decode("utf-8")
# print('html:{}'.format(html))
# 2、解析网页
items = WeixinParser().parse_index(html)

# 3、输出数据
date_str = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
fileName = date_str + ".json"
file = open(fileName, "w", encoding='utf-8')
# json.dump(json_str, file)
file.write(json.dumps(items, indent=4, ensure_ascii=False))
file.close()

# for item in items: 
    # print(item)
# {'title': '百度一下，你就知道'}
