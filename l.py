#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2


def openNullProxy():
    # (null) proxy handler
    null_proxy_handler = urllib2.ProxyHandler({})
    proxy_opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(proxy_opener)


def GetResponseFromSite(url):
    # credential to send to log in?
    # request_credential = {"AUTHENTICATION.LOGIN": "", "AUTHENTICATION.PASSWORD": ""}
    request_credential = {"AUTHENTICATION.PASSWORD": ""}
    value_credential = urllib.urlencode(request_credential)

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
        "Connection": "Keep-Alive"
    }

    request_POST = urllib2.Request(url, value_credential, request_headers)
    response_POST = urllib2.urlopen(request_POST)

    print dir(response_POST)
    print "-----------------------"
    print response_POST.read()
    # print response_POST.data


# ---------------------------MAIN PROGRAMME--------------------------------
# url of the site to log in
url = ""

GetResponseFromSite(url)
