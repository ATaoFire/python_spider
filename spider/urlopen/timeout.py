import socket
import urllib.request
import urllib.error
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.0001)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("Time out")
