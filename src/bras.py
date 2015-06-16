#coding:utf-8

import requests
import time
from optparse import OptionParser

try:
    from conf import USERNAME,PASSWORD
except:
    print "Unable to load username and password"


def main():
    opt_parser = OptionParser()
    opt_parser.add_option('-c', action='store_true', default=True, help='make bras connected') 
    opt_parser.add_option('-d', action='store_true', help='make bras disconnected')
    opt_parser.add_option('-u', '--username', help='your acount name')
    opt_parser.add_option('-p', '--password', help='your account password')
    opts, args = opt_parser.parse_args()
    if opts.d:
        disconnect_bras()
    else:
        connect_bras(opts)


def connect_bras(opts):
    if opts.username:
        username = opts.username
    else:
        username = USERNAME
    if opts.password:
        password = opts.password
    else:
        password = PASSWORD
    print username,password
    url = 'http://p.nju.edu.cn/portal_io/login'
    formdata= 'username=%s&password=%s' % (username, password)
    url = url + '?' + formdata
    print formdata
    try:
        #r = requests.post(url, data=formdata)
        r = requests.get(url)
        content = r.content
        print content
    except:
        print 'Please try again or check your options'


def disconnect_bras():
    for _ in range(3):
        url = 'http://p.nju.edu.cn/portal/portal_io.do'
        formdata = 'action=logout'
        try:
            r = requests.post(url,data=formdata)
        except:
            print 'Please try again or check your options'


if __name__ == "__main__":
    main()
