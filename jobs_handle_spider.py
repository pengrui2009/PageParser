
# page_parser 包使用示例：6行代码写爬虫

import requests
from page_parser.weixin_parser import WeixinParser

# 1、下载网页
response = requests.get("https://mp.weixin.qq.com/s/fZp8gs-Uayckuia6WJ89ag")
html = response.content.decode("utf-8")
print('html:{}'.format(html))
# 2、解析网页
items = WeixinParser().parse_index(html)

# 3、输出数据
for item in items: print(item)
# {'title': '百度一下，你就知道'}
