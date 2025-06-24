from pydoc import pager
from urllib import request

#requests 는 외장객체 , request는 내장객체

site = request.urlopen('https://www.google.com')

page = site.read()
print(page)

print('*' * 100)
print(site.getheaders())

for data in site.getheaders():
    print(data[0],'>>',data[1])