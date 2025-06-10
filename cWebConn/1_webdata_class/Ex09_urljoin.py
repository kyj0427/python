"""
 urllib.parse.urljoin() : 상대경로를 절대경로로 변화하는 함수
"""

'''
from urllib import  parse

baseUrl = 'http://www.example.com/html/ict/a.html'

print(parse.urljoin(baseUrl, 'b.html'))

print(parse.urljoin(baseUrl, 'sub/c.html'))
print(parse.urljoin(baseUrl, '/sub/d.html'))

print(parse.urljoin(baseUrl, '../sub/e.html'))
print(parse.urljoin(baseUrl, '../temp/f.html'))

print(parse.urljoin(baseUrl, 'http://www.naver.com'))
'''


#import 하는 방식에 따라 사용하는 코딩 방법이 달라진다
from urllib.parse import urljoin
baseUrl = 'http://www.example.com/html/ict/a.html'
print(urljoin(baseUrl, 'b.html'))



