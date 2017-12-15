def multi():
    first = 1
    last = 20
    lst = list(range(int(first), int(last)))

    for i in map(printprime,lst) :
        print(i)



def printprime(i):
        if (i % 7 == 0):
            return 'multi'
        elif (i % 13 == 0):
            return 'attribution'
        elif (i % 3 == 0) and (i % 5 == 0):
            return 'Multi-Attribution'
        else:
            return i


#multi()

import urllib3 #https://pypi.python.org/pypi/urllib3
import re
import requests
#from bs4 import Beautifulsoup as bs

azurl = 'http://www.azlyrics.com/lyrics'
band='beatles'
song ='letitbe'
http = urllib3.PoolManager()
url ='{}/{}/{}.html'.format(azurl,band,song)
r=http.request('GET',url)
#site = urllib3.open(url)
print(r.data)

