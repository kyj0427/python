"""
http://www.seoul.go.kr > 청사안내 > 자치구
https://www.seoul.go.kr/seoul/autonomy.do

BeautifulSoup  : 파서를 이용해서 html 의 요소를 추출하게 해주는 모듈
        - 단점은 개행문자를 고려해야 한다
Tag : 태그
NavigableString : 원래는 tag 사이의 문자열

#  xpath를 사용하면 개행문자를 고려하지 않아도 된단다
#  https://developer.mozilla.org/ko/docs/XPath
"""

from urllib import request
from bs4 import BeautifulSoup

html = 'http://www.seoul.go.kr/seoul/autonomy.do'
site = request.urlopen(html)
site1=site.read()

soup = BeautifulSoup(site1,"html.parser")

# 아래 리스트에 각 구청의 상세 정보를 저장하고 출력하기
구청이름=[]
구청주소=[]
구청전화번호=[]
구청홈페이지=[]


'''
1. 추출한 결과를 위 리스트에 저장한다.

2. 리스트 출력 결과 예시- 아래처럼 각 구청의 정보를 추출
      ex)
      구청이름 : 강동구
      구청주소 : (우) 04558 / 서울시 중구 창경궁로 17 (예관동)
      구청전화번호 : TEL. 02-3396-4114
      구청홈페이지 : http://www.junggu.seoul.kr
'''

#1

for i in range(1,26): #1~25 까지 숫자 반복문
    tmp1 = soup.select("#district%d > strong" % i ) # %가 format보다 속도가 빠르다
    #print(tmp1[0].text)
    tmp2 = soup.select('#district%d > ul > li:nth-child(1)' % i)
    tmp3 = soup.select('#district%d > ul > li:nth-child(2)' % i)
    tmp4 = soup.select('#district%d > ul > li:nth-child(3)' % i)
    print( "구청이름 :",tmp1[0].text.strip(),'\n'
          ,"구청주소 :",tmp2[0].text.strip(),'\n'
          ,"구청전화번호 :",tmp3[0].text.strip(),'\n'
          ,"구청홈페이지 :",tmp4[0].text.strip())

    구청이름.append(tmp1[0].text) #태그와 태그사이에 들어있는
    구청주소.append(tmp2[0].text)
    구청전화번호.append(tmp3[0].text)
    구청홈페이지.append(tmp4[0].text)




