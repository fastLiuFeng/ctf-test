import urllib.request

'''
response = urllib.request.urlopen("http://104.129.186.123:5000/iptest")
data = response.read()
print(data)
print(data.decode("utf-8"))
'''

ua_headers = {
    'User-Agent': 'kid_mozilla',
#    'X-Forwarded-For': '4.4.4.4',
}
#request = urllib.request.Request("http://104.129.186.123:5000/iptest", headers=ua_headers)
request = urllib.request.Request("http://104.129.186.123:5000/ipheader", headers=ua_headers)
response = urllib.request.urlopen(request)
data = response.read()
print(data.decode("utf-8"))
