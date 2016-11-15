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


def ReqPOST(url):
    # credential to send to log in?
    # request_credential = {"AUTHENTICATION.LOGIN": "", "AUTHENTICATION.PASSWORD": ""}
    value_credential = {
        "login": ".",
        "foolAutofillFromBrowser": "",
        "password": "?",
        "sub_auth": "Login"
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
    response_S = s.get(url, params=payload, headers=headers, verify=False)  # params=payload
    # s.headers.update
    print response_S.text

    # r = requests.post(url, data=payload)

# ---------------------------MAIN PROGRAMME--------------------------------
# url of the site to log in
url = ""
# ReqGET(url)
# ReqPOST(url)
Sessionlogin(url)
Sessionlogin(url)
