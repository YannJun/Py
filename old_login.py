#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import cookielib
import json
import requests
import login

# LoginForm[password]   
# LoginForm[rememberMe]  0
# LoginForm[username]   
# _csrf  dy5LRC1hV28.ZwUQQlRgQiFtMndqUyJaPlo/E0M7FR5FfAwbSRgwAA==
# login-button   登 录

# site to log in
url = 'httqsd/qsdin'
# file to stock the cookies
filename = 'cookie.txt'
# headers setting
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    #"Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8",
    #"Cache-Control": "max-age=0",
    "Connection": "keep-Alive",
    "Content-Type": "application/x-www-form-urlencoded",
    #"Cookie": "MIBLayout=%7B%22useLayout%22%3A%20false%7D; IBCApplication=kcku4e5bg0q3nsiu902d54hvv1",
    "Host": "mib",
    "Origin": "htqsd",
    "Referer": "https://mqsdion",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36"
}
# disable the urllib3 warnings when using old version python
requests.packages.urllib3.disable_warnings()
# 建立一个会话，可以把同一用户的不同请求联系起来；直到会话结束都会自动处理cookies
s = requests.Session()
# 建立LWPCookieJar实例，可以存Set-Cookie3类型的文件。
s.cookies = cookielib.MozillaCookieJar(filename)


def Login(url, username, password):
    """
    Enter your username and password to log in
    """
    print 'Loging on toqsd), Please wait...'
    # data to send to the site in case of login
    data = {
        "login": username,
        "foolAutofillFromBrowser": "",
        "password": password,
        "sub_auth": "Login"
        # '_csrf': Getcsrf(),
    }

    try:
        # send the request to the site to log in
        result = s.post(url, data=data, headers=headers, verify=False)  # allow_redirects=True,
        # print the HTML source of the page after login
        print result.text
    # Error check when loging
    except requests.RequestException as e:
        print e
        print "There was an ambiguous exception that occurred while handling your request."

    except requests.ConnectionError as e:
        print "A Connection error occurred."

    except requests.HTTPError as e:
        print "An HTTP error occurred."

    except requests.URLRequired as e:
        print "A valid URL is required to make a request."

    except requests.TooManyRedirects as e:
        print "Too many redirects."

    except Exception as e:
        raise

    # save cookies to local storage to maintain the seesion (connection)
    s.cookies.save(ignore_discard=True, ignore_expires=True)


def SessionMaintain(none_login_url):
    """
    Maintain the previous session with cookies
    """
    print 'Session recovering...'

    try:
        # Try to load the cookies stocked in a local file
        print 'Loading cookies...'
        s.cookies.load(filename=filename, ignore_discard=True, ignore_expires=True)
        print 'Cookie loaded with success, waiting for the response'
        # When cookies loaded, go to the site after login
        rep = s.get(none_login_url, verify=False)
        # print the page's HTML
        print rep.text
        # if rep.cookies.get_dict():
        #     self.cookies.update(r.cookies)
    # Error check when loging
    except requests.RequestException as e:
        print e
        print "There was an ambiguous exception that occurred while handling your request."

    except requests.ConnectionError as e:
        print "A Connection error occurred."

    except requests.HTTPError as e:
        print "An HTTP error occurred."

    except requests.URLRequired as e:
        print "A valid URL is required to make a request."

    except requests.TooManyRedirects as e:
        print "Too many redirects."

    except Exception as e:
        raise

    # save cookies to local storage to maintain the seesion (connection)
    session.cookies.save(ignore_discard=True, ignore_expires=True)


# ---------------------------MAIN PROGRAMME--------------------------------
if __name__ == '__main__':
    pass
    # Login with an account
    # Login(url, username='', password='?')

    # home_url = "hqsd
    # SessionMaintain(home_url)
