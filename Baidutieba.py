# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Baidutieba:

    def __init__(self):
        self.base_url = 'https://tieba.baidu.com'
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.pageurl = 'https://tieba.baidu.com/f?'
        self.proxies = {'HTTP': '118.190.199.55:80'}

    def getpageurl(self, url, params):

        response = requests.get(url, headers=self.headers,
                                params=params, proxies=self.proxies)
        response.encoding = 'utf-8'
        html = response.text
        parseHtml = etree.HTML(html)
        print(html)
        r_list = parseHtml.xpath(
            '//div[@class="t_con cleafix"]/div/div/div/a/@href')
        print(r_list)
        for r in r_list:
            url = self.base_url + r
            self.getimageurl(url)

    def getimageurl(self, url):

        response = requests.get(url, headers=self.headers)
        response.encoding = 'utf-8'
        html = response.text
        parseHtml = etree.HTML(html)
        r_list = parseHtml.xpath('//img[@class="BDE_Image"]/@src')
        for i in r_list:
            self.writeimage(i)

    def writeimage(self, url):

        response = requests.get(url, headers=self.headers)
        response.encoding = 'utf-8'
        html = response.content
        filename = url[-10:]
        with open(filename, 'wb')as f:
            f.write(html)

    def workit(self):
        name = input('请输入要爬取图片的贴吧名')
        begin = int(input('请输入起始页'))
        end = int(input('请输入终止页'))
#        name='美女'
#        begin=1
#        end=3

        for i in range(begin, end + 1):
            pn = (i - 1) * 50
            params = {'kw': name,
                      'pn': str(pn),
                      }
            print(pn, params)
            self.getpageurl(self.pageurl, params)


if __name__ == '__main__':
    baidu = Baidutieba()
    baidu.workit()
