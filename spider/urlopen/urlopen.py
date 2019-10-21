import urllib.request
#使用urlopen时需要引入ssl，ssl._create_default_https_context = ssl._create_unverified_context

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

response = urllib.request.urlopen('https://www.python.org')
#打印抓取的内容
# print(response.read().decode('utf-8'))
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))