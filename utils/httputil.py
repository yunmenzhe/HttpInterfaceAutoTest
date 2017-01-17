# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse


# get取网页数据
def geturl(url, data={}, headers={}):
    html = ""
    try:
        params=urllib.parse.urlencode(data).encode(encoding='UTF8')
        req=urllib.request.Request("%s?%s" % (url, params))
        #设置headers
        for i in headers:
            req.add_header(i,headers[i])
            r=urllib.request.urlopen(req)
        html =r.read()
        return html.decode("utf8")
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))
    return html


def posturl(url, data={}, headers={}):
    try:
        params=urllib.parse.urlencode(data).encode(encoding='UTF8')
        req = urllib.request.Request(url, params, headers)
        r = urllib.request.urlopen(req)
        html =r.read()
        return html.decode("utf8")
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))

# 医生登录开始
ID = ""
token = ""
doctorId = ""
deviceSN = "F2LR36GCGRWM"
phoneNum = 13811984643
password = 123456
adServerHost = "http://10.9.2.10:8090/"
passwordServerHost = "http://localhost:8081/"
# 请求头
headers = {
    '_c': "2222",
    '_m': "90:67:1c:cc:98:2c",
    '_p': "1",
    '_v': "2.6.6",
    'userType': "d"
}
# 获取基本数据
loginKey = geturl(adServerHost + "login/genLoginKey", {'phoneNum': phoneNum}, headers)
import json
loginKeyJsonData = json.loads(loginKey)
loginKeyData = loginKeyJsonData.get("data")
loginKey = loginKeyData[0].get("loginKey")
ID = loginKeyData[0].get("doctorId")
# 获得密码加密结果
encryptedPwd = geturl(passwordServerHost + "passwordEncrypt/getEncryptedPWD", {'password': password}, headers)
# 开始登录
loginParamter = {
    'doctorId': ID,
    'loginKey': loginKey,
    'password': encryptedPwd,
    'deviceSN': deviceSN
}
loginInfo = geturl(adServerHost + "login/login", loginParamter, headers)
loginInfoJsonData = json.loads(loginInfo)
loginInfoData = loginInfoJsonData.get("data")
token = loginInfoData[0].get("token")
doctorId = loginInfoData[0].get("doctorId")
# 医生登录结束,保存相关数据

defaultParameter = {
    'token': token,
    'id': doctorId,
    'doctorId': doctorId
}
print(geturl(adServerHost + "user/detail", defaultParameter, headers))