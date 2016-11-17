#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
# import urllib
# import urllib2
# import re
import cookielib
import requests


class Login(object):
    # the login site and the post login site (home pqge)
    login_url = "AZE"
    home_url = "httAZE"

    # path of the cookies file
    path = os.path.dirname(os.path.abspath(__file__))
    filePath = path + 'cookie.txt'

    # headers setting
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        # "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "en-US,en;q=0.8",
        # "Cache-Control": "max-age=0",
        "Connection": "keep-Alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "mib",
        "Origin": "htAZE",
        "Referer": "httpAZEZEon",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36"
    }

    def __init__(self, mode):
        """
        mode 0: log in with credentials
        mode 1: session recovery by cookies
        """
        self.mode = mode

    def sessionBuild(self):
        """
        Build up and return a session that automatically deal with the cookies
        """
        # disable the urllib3 warnings when using old version python
        requests.packages.urllib3.disable_warnings()
        # set up session that can automatically deal with the cookies
        session = requests.Session()
        # set up an object to stock the cookies
        session.cookies = cookielib.MozillaCookieJar(Login.filePath)
        return session

    def loginByAuthentication(self):
        """
        Enter your username and password to log in
        """
        # username + password
        username = raw_input("Please enter your login :\n")
        password = raw_input("Then please enter your password :\n")
        # data to send to the site in case of login
        dataAndCredentials = {
            "login": username,
            "foolAutofillFromBrowser": "",
            "password": password,
            "sub_auth": "Login"
        }
        # Start to log on
        try:
            print 'Loging on to XXX Please wait...'
            # Send the request to the site to log on
            response = session.post(Login.login_url, data=dataAndCredentials, headers=Login.headers, verify=False)
            # Print the HTML source of the page after login
            print response.text

        # Error check when loging
        except requests.RequestException as e:
            print "There was an ambiguous exception that occurred while handling your request."
            print "Error details : " + e

        except requests.ConnectionError as e:
            print "A Connection error occurred."
            print "Error details : " + e

        except requests.HTTPError as e:
            print "An HTTP error occurred."
            print "Error details : " + e

        except requests.URLRequired as e:
            print "A valid URL is required to make a request."
            print "Error details : " + e

        except requests.TooManyRedirects as e:
            print "Too many redirects."
            print "Error details : " + e

        except Exception as e:
            raise

        else:
            # save cookies to local storage to maintain the seesion
            # (connection)
            session.cookies.save(ignore_discard=True, ignore_expires=True)

        def SessionMaintain(self, home_url):
            """
            Maintain the previous session with cookies
            """
            print 'Session recovering...'

            try:
                # Try to load the cookies stocked in a local file
                print 'Loading cookies...'
                session.cookies.load(
                    filename=Login.filePath, ignore_discard=True, ignore_expires=True)
                print 'Cookie loaded with success, waiting for the response'
                # When cookies loaded, go to the site after login
                response = session.get(Login.home_url, verify=False)
                # Print the page's HTML
                print response.text
                # if rep.cookies.get_dict():
                #     self.cookies.update(r.cookies)

            # Error check when loging
            except requests.RequestException as e:
                print "There was an ambiguous exception that occurred while handling your request."
                print "Error details : " + e

            except requests.ConnectionError as e:
                print "A Connection error occurred."
                print "Error details : " + e

            except requests.HTTPError as e:
                print "An HTTP error occurred."
                print "Error details : " + e

            except requests.URLRequired as e:
                print "A valid URL is required to make a request."
                print "Error details : " + e

            except requests.TooManyRedirects as e:
                print "Too many redirects."
                print "Error details : " + e

            except Exception as e:
                raise
            else:
                # save cookies to local storage to maintain the seesion
                # (connection)
                session.cookies.save(ignore_discard=True, ignore_expires=True)

        def Getcsrf(self):
            """
            Get the _csrf parameter (this function is not necessary for the moment)
            """
            response = session.get(self.login_url, headers=Login.headers)
            html = response.text
            print html
            get_csrf_pattern = re.compile(
                r'< the match pattern for the regular expression search >')
            '''
               find all the information corresponding to the pattern, and return a list.
               Normally, there'll be just one element in the list. So take the first element
            '''
            _csrf = re.findall(get_csrf_pattern, html)[0]
            # returloginn the element extracted previously
            return _csrf


class Extract(object):

    def __init__(self):
        pass


class WriteExcel(object):

    def __init__(self):
        pass

# print os.path.dirname(os.path.abspath(__file__))
# print os.getcwd()
