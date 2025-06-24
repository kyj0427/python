"""
    HTML 내부에 있는 링크를 추출하는 함수
        - a 링크 연결된 모든 파일을 가져오기
"""

from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
# 함수 함수명 (인자)
def enum_links(html,base):
    #-------------------------------------
    # 파이썬 대표 파싱
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('a')
    #print(len(links))
    # print(links[0])
    # print(links[0].attrs['href'])
    # print(parse.urljoin( base, links[0].attrs['href']))



#해당페이지에서 a태그에 링크들을 추출하여 list에 저장해서 리턴해줌
    result = []
    for link in links:
        href = link.attrs['href']
        url = parse.urljoin( base, href)
        #print(url)
        result.append(url)

    return result

#__내부변수__ 특별한 목적에서 사용
if __name__ == '__main__':
    url = 'https://docs.python.org/3.7/library/'
    response = request.urlopen(url)   # urllib.request.urlopen() : BeautifulSoup을 통해 html 파서할(데이타를 가져올) 대상
    result = enum_links(response, url)
    print(result)