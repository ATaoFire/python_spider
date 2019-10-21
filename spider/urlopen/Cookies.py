import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')

for item in cookie:
    print(item.name + "=" + item.value)


#保存cookie到本地
#命名文件名称
cookie_jar = http.cookiejar.LWPCookieJar(filename='baidu.txt')
#创建handler
cook_handler = urllib.request.HTTPCookieProcessor(cookie_jar)
#创建opener
opener = urllib.request.build_opener(cook_handler)

req = urllib.request.Request('http://www.baidu.com')

res = opener.open(req)

cookie_jar.save()


cookie_jar.save(ignore_discard=True, ignore_expires=True)

