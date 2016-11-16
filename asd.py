#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import cookielib
import json
import requests

# LoginForm[password]	wodingni1937
# LoginForm[rememberMe]	 0
# LoginForm[username]	 498651225@qq.com
# _csrf	 dy5LRC1hV28.ZwUQQlRgQiFtMndqUyJaPlo/E0M7FR5FfAwbSRgwAA==
# login-button	 登 录

# url of the site to log in
url = "http://home.51cto.com/index?reback=http://www.51cto.com/"
# file to stock the cookies
filename = 'cookie'
# headers setting
headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-Alive",
    # "Host": "",
    "Referer": url,
    # "Upgrade-Insecure-Requests": 1,
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
    # "Content-Type": "text/html"
}

# 建立一个会话，可以把同一用户的不同请求联系起来；直到会话结束都会自动处理cookies
session = requests.Session()
# 建立LWPCookieJar实例，可以存Set-Cookie3类型的文件。
# 而MozillaCookieJar类是存为'/.txt'格式的文件
session.cookies = cookielib.LWPCookieJar(filename)
# 若本地有cookie则不用再post数据了
try:
    print 'Loading cookies...'
    session.cookies.load(
        filename=filename, ignore_discard=True, ignore_expires=True)
    print 'Cookie loaded with success'
    # rep = session.get(
    #     'http://home.51cto.com/index?reback=http://www.51cto.com/',)
    # rep.encoding = 'utf-8'
    # print rep.encoding
    # print rep.text.encode('utf-8')
    # # if rep.cookies.get_dict():
    # #     self.cookies.update(r.cookies)
except:
    print 'Cookie未加载！或 Response出错'


def Getcsrf():
    """
    获取参数_csrf
    """
    response = session.get(
        'http://home.51cto.com/index?reback=http://www.51cto.com/', headers=headers)
    response.encoding = 'utf-8'
    html = response.text.encode('utf-8')
    print html
    get_csrf_pattern = re.compile(
        r'<input type="hidden" value="(.*?)" name="_csrf">')
    _csrf = re.findall(get_csrf_pattern, html)[0]
    return _csrf


def Login(url, username, password):
    """
    输入自己的账号密码，模拟登录51cto
    """
    print '登录中...'
    data = {
        "LoginForm[password]": password,
        "LoginForm[rememberMe]": 0,
        "LoginForm[username]": username,
        '_csrf': Getcsrf(),
        "login-button": "登 录",
    }
    # 若不用验证码，直接登录
    try:
        result = session.post(url, data=data, headers=headers)
        print (json.loads(result.text))['msg']
    # 要用验证码，post后登录
    except:
        print 'something is wrong'
        print result.text.encode('utf-8')  # .decode('utf-8')
        print dir(result.text)
        print dir(result)
        # print result.decode('utf-8')
        # print (json.loads(result.text))['msg']
    # 保存cookie到本地
    session.cookies.save(ignore_discard=True, ignore_expires=True)


def ReqPOST(url):
    # credential to send to log in?
    # request_credential = {"AUTHENTICATION.LOGIN": "", "AUTHENTICATION.PASSWORD": ""}
    value_credential = {
        "LoginForm[password]": ".",
        "LoginForm[rememberMe]": "",
        "LoginForm[username]": "?",
        "login-button": "登 录"
    }
    # encode the data
    data_credential = urllib.urlencode(value_credential)

    # data for debug (test data)
    # value_debug = {"username": "qsd.yang", "password": "############"}
    # data_debug = urllib.urlencode(value_debug)

    # header setting
    request_headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        # "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "en-US,en;q=0.8",
        "Connection": "keep-Alive",
        "Host": "",
        "Referer": url,
        "Upgrade-Insecure-Requests": 1,
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
        # "Content-Type": "text/html"
    }

    request_POST = urllib2.Request(url, data_credential, request_headers)

    try:
        response_POST = urllib2.urlopen(request_POST)
    except urllib2.HTTPError as e:
        if e.code == 404:
            print "Error 404, Page not found"
            print "cause : " + e.reason
    else:
        print "===================================Login Success=======================================\n"
        print response_POST.read()


def ReqGET(url):
    request_GET = urllib2.Request(url)
    response_GET = urllib2.urlopen(url)
    print "-----------------------"
    print response_GET.read()


def Sessionlogin(url):
    payload = {
        "login": "",
        "foolAutofillFromBrowser": "",
        "password": "?",
        "sub_auth": "Login"
    }
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        # "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "en-US,en;q=0.8",
        "Connection": "keep-Alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "",
        "Origin": "",
        "Referer": url,
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36"
        # "Content-Type": "text/html"
    }
    s = requests.Session()
    response_S = s.get(url, params=payload, headers=headers,
                       verify=False)  # params=payload
    # s.headers.update
    print response_S.text

    # r = requests.post(url, data=payload)

# ---------------------------MAIN PROGRAMME--------------------------------
if __name__ == '__main__':
    Login(url, username='', password='')

    home_url = 'http://home.51cto.com/index?reback=http://www.51cto.com/'
    resp = session.get(home_url, headers=headers, allow_redirects=True)
    resp.encoding = 'utf-8'
    print resp.text.encode('utf-8')
