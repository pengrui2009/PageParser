# -*- coding: utf-8 -*-

# @Date    : 2018-10-13
# @Author  : Peng Shiyu

from parsel import Selector


class WeixinParser(object):
    """
    微信网：https://mp.weixin.qq.com/
    """

    @staticmethod
    def parse_index(html):
        """
        解析主页：https://mp.weixin.qq.com/
        :param html: {str} 网页文本
        :return: {iterator} 抽取的内容
        """
        sel = Selector(html)
        
        title = sel.css("title::text").extract_first()
        item = {
            "title": title
        }
        yield item


if __name__ == '__main__':
    import requests

    response = requests.get("https://mp.weixin.qq.com/")
    response.encoding = response.apparent_encoding
    items = WeixinParser().parse_index(response.text)
    for item in items:
        print(item)

        # {'title': '百度一下，你就知道'}
