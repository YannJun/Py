#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
import json
import requests


def SaveCookies(url):
    # 设置保存cookie的文件，同级目录下的cookie.txt
    filename = 'cookie.txt'
    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookielib.MozillaCookieJar(filename)
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    cookie_handler = urllib2.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    cookie_opener = urllib2.build_opener(handler)
    # 创建一个请求，原理同urllib2的urlopen
    response = opener.open(url)
    # 保存cookie到文件
    cookie.save(ignore_discard=True, ignore_expires=True)


def OpenNullProxy():
    # (null) proxy handler
    null_proxy_handler = urllib2.ProxyHandler({})
    proxy_opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(proxy_opener)


def GetResponseFromSite(url):
    # credential to send to log in?
    # request_credential = {"AUTHENTICATION.LOGIN": "", "AUTHENTICATION.PASSWORD": ""}
    #request_GET = urllib2.Request(url)
    # client = requests.session()
    # response_GET = urllib.urlopen(url)

    value_credential = {
        "LoginForm[username]": "@qq.com",
        "LoginForm[password]": "",
        "LoginForm[rememberMe]": 0,
        "login-button": "登 录"
    }
    data_credential = urllib.urlencode(value_credential)

    # data for debug (test data)
    value_debug = {"username": "qsd.yang", "password": "############"}
    data_debug = urllib.urlencode(value_debug)

    # header setting
    request_headers = {
        #"Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": url,
        "Host": "log.51cto.com",
        "Connection": "keep-Alive"
    }

    request_POST = urllib2.Request(url, data_credential, request_headers)
    request_GET = urllib2.Request(url)
    response = urllib2.urlopen(request_GET)

    print "-----------------------"
    print dir(request_GET)
    print "-----------------------"
    print dir(response)
    print "-----------------------"
    print dir(response.headers)
    print "-----------------------"
    print response.headers
    # print response.read()
    # print response_POST.data


def Sessionlogin(url):
    s = requests.Session()
    print s.get(url).cookies['csrf-token']

    #response_S = s.get(url)
    #csrf_token = response_S.cookies['csrf']
    # print dir(response_S), response_S.cookies

# ---------------------------MAIN PROGRAMME--------------------------------
# url of the site to log in
url = "http://home.51cto.com/index/?reback=http%3A%2F%2Fedu.51cto.com%2Fcenter%2Fuser%2Findex%2Flogin-success%3Fsign%3D6f2dzemoA77jungBNlad73PnT0FSKJT8Kfl74X15sJPuIX5HN12pPHDc3A51vAdkxq403ZKTdf774gX1dNpLiTZH5r8ysjaER5qTZ2SuHvVm6vvcLRyL2I_VZxlRi_ZUo4HB%26client%3Dweb"

Sessionlogin(url)
