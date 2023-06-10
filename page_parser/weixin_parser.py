# -*- coding: utf-8 -*-

# @Date    : 2018-10-13
# @Author  : rui.peng


import datetime
from parsel import Selector

class JobDescribe():
    def __init__(self, title, content, require, datetime, salares, distance, address, 
                 contract, comments, iconurl, userId, completed, createTime, completeTime, expired) -> None:
        self._title = title
        self._content = content
        self._requirements = require
        self._datetime = datetime
        self._salares = salares
        self._distance = distance
        self._address = address
        self._contract = contract
        self._comments = comments
        self._iconurl = iconurl
        self._userId = userId
        self._completed = completed
        self._createTime = createTime
        self._completeTime = completeTime
        self._expired = expired


    def GetJobElem(self) :
        return {'': 0, '': 0, 'expired': self._expired}

def parse_title(str):
    result = None
    if '招聘岗位' in str :
        result = str        
    return result

def parse_datetime(str) :
    result = None
    if '工作时间' in str :
        result = str        
    return result

def parse_content(str) :
    result = None
    if '工作内容' in str :
        result = str        
    return result

def parse_salares(str) :
    result = None
    if '工资待遇' in str :
        result = str        
    return result

def parse_distance(str) :
    result = None
    if '工作地点距离' in str :
        result = str        
    return result

def parse_requirements(str) :
    result = None
    if '招聘人数' in str :
        result = str        
    return result

def parse_address(str) :
    result = None
    if '工作地点' in str :
        result = str        
    return result

def parse_contrace(str) :
    result = None
    if '报名加微信' in str or '报名微信' in str or '工作时间' in str or '微信' in str :
        result = str        
    return result

def parse_comments(str) :
    result = None
    if '工作要求' in str :
        result = str        
    return result

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
        
        # title = sel.css('//*[@id="js_content"]').extract_first()
        # contents = sel.xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]').extract_first()
        sections = sel.xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/section')
        # print(len(sections))
        index = 1
        items = []
        current_datetime = datetime.datetime.now() + datetime.timedelta(days=1)
        # current_datetime.datetime.timedelta(days=1)
        current_datetime.replace(hour=23, minute=59, second=59)
        expired_time = int((current_datetime - datetime.datetime(1970, 1, 1)).total_seconds())
        datestr = current_datetime.strftime('%Y-%m-%d')
        print('{} {}'.format(datestr, expired_time))
        
        for section in sections:
            # print('section:{}'.format(section))
            ps = section.xpath('//*[@id="js_content"]/section['+ str(index) + ']/section/section/p')
            # print('len(ps):{}'.format(len(ps)))
            index1 = 1
            jobinfo = {'userId': {'$oid': '64537dc3e766bb008529e762'}, 'title': '', 'content': '', 'datetime': ''
                     , 'salares': '', 'distance': '' , 'address': '', 'contract': '', 'comments': '', 
                     'completed': 'false', 'expired': 0}
            for p in ps :
                p_text = p.xpath('//*[@id="js_content"]/section['+ str(index) + ']/section/section/p[' + str(index1) + ']/span/text()').extract_first()
                print('{}'.format(p_text))
                if p_text != None :
                    title = parse_title(p_text)
                    if title != None :
                        jobinfo['title'] = title                    
                    # parse content
                    workcontent = parse_content(p_text)
                    if workcontent != None :
                        jobinfo['content'] = workcontent
                    # parse requirements
                    requirements = parse_requirements(p_text)
                    if requirements != None :
                        jobinfo['requirements'] = requirements
                    # parse datetime
                    worktime = parse_datetime(p_text)
                    if worktime != None :
                        jobinfo['datetime'] = worktime
                    # parse salares
                    worksalares = parse_salares(p_text)
                    if worksalares != None :
                        jobinfo['salares'] = worksalares
                    # parse distance
                    workdistance = parse_distance(p_text)
                    if workdistance != None :
                        jobinfo['distance'] = workdistance
                    # parse address
                    workaddress = parse_address(p_text)
                    if workaddress != None :
                        jobinfo['address'] = workaddress
                    # parse contract
                    workcontract = parse_contrace(p_text)
                    if workcontract != None :
                        jobinfo['contract'] = workcontract
                    # parse comments
                    workcomments = parse_contrace(p_text)
                    if workcomments != None :
                        jobinfo['comments'] = workcomments                    

                index1 = index1 + 1
            jobinfo['expired'] = expired_time
            items.append(jobinfo)
            index = index+1
            print('**********************************')
        return items            
        # print(type(contents))
        
        # for content in contents :
        #     print('{}'.format(content))
        # for i in range(len(contents)) :
        #     print('+++++++++++++++++++++')
        #     xpath_str = '//*[@id="js_content"]/section['+ str(i) + ']/section/section/p'
        #     # print('xpath:{}'.format(xpath_str))
        #     section_p = contents.xpath(xpath_str)
            
        #     # section_num_str = '//*[@id="js_content"]/section['+ str(i) + ']/section/section/p'
        #     # section_num = len(section.xpath(section_num_str))
        #     # print('section_num:{}'.format(section_num))
        #     # print('*********************, len:{}'.format(len(section)))
        #     for index in range(len(section_p)) :
        #         p_xpath_str = '//*[@id="js_content"]/section['+ str(i) + ']/section/section/p[' + str(index) + ']/span/text()'
        #         p = section.xpath(p_xpath_str).extract_first()
        #         print('p:{}'.format(p))
        #         # if p == None:
        #         #     break
            
        #     # print('section:{}'.format(section))
        #     # if section == None :
        #         # print('section is none')
        #         # break

        # yield item


if __name__ == '__main__':
    import requests

    response = requests.get("https://mp.weixin.qq.com/")
    response.encoding = response.apparent_encoding
    items = WeixinParser().parse_index(response.text)
    for item in items:
        print(item)

        # {'title': '百度一下，你就知道'}
