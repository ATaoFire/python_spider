import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))