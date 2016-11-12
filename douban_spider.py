# coding=utf-8
# usr/bin/eny python

import urllib.request
import json
from html.parser import HTMLParser
'''
                    用HTMLParser处理从豆瓣网上爬取的数据 ( OK )
'''
class MovieParser(HTMLParser):  #解析器继承于HTMLParser
    def __init__(self):
        HTMLParser.__init__(self)       #调用父类的一个构造函数
        self.movies = []

    def handle_starttag(self,tag,attrs):      #解析数据的函数
        def _attr(attrlist,attrname):        #attrlist是一个属性列表,attrname是要提取的属性的值。对attrlist和attrname进行匹配
            for attr in attrlist:   # 0表示属性的名称，1表示属性的值
                if attr[0] == attrname:   #如果属性名称和要的名称是一样的，则返回这个属性的值
                    return attr[1]
            return None       #没找到名称则返回空的


        # print(tag)
        if tag =='li' and _attr(attrs,'data-score'):    #只解析li 而且里面的属性data-title不为空
            movie = {}
            movie['title'] = _attr(attrs,'data-title')
            # print('%s',movie['title'])
            movie['score'] = _attr(attrs, 'data-score')
            movie['director'] = _attr(attrs, 'data-director')
            movie['actors'] = _attr(attrs, 'data-actors')
            self.movies.append(movie)                    #把提取出来的电影放到列表里面去
            print('%(title)s|%(score)s|%(director)s|%(actors)s|' % movie)


def nowplaying_movies(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
    req = urllib.request.Request(url,headers=headers)
    s = urllib.request.urlopen(req)
    parser = MovieParser()        #MovieParser作为一个解析器
    parser.feed(s.read().decode())      #给解析器喂网页数据
    s.close()
    return parser.movies

if __name__ == '__main__':
    url ='http://movie.douban.com/nowplaying/xiamen/'
    movies = nowplaying_movies(url)

    # print('%s' % json.dumps(movies, sort_keys=True,indent=4,separators=(',',': ')))   #json，用于字符串 和 python数据类型间进行转换