# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse


# get取网页数据
def geturl(url, data={}, headers={}):
    try:
        params = urllib.parse.urlencode(data)
        req = urllib.request.Request("%s?%s" % (url, params))
        # 设置headers
        for i in headers:
            req.add_header(i, headers[i])
        r = urllib.request.urlopen(req)
        html = r.read()
        return html.decode("utf8")
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))


def posturl(url, data={}, headers={}):
    try:
        params = urllib.parse.urlencode(data)
        req = urllib.request.Request(url, params, headers)
        r = urllib.request.urlopen(req)
        html = r.read()
        return html.decode("utf8")
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))

