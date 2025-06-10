
# urlretrieve(): 파일로 바로 저장
# urlopen(): 파일로 바로 저장하기 않고 메모리에 로딩을 한다.

""" [참고] 파일저장 기본방식
    f = open('a.txt','w')
    f.write("테스트 내용")
    f.close()

    위의 과정을 with 문으로 간략하게 close 필요없음
    with open("a.txt","w") as f:
        f.write("테스트 내용")
"""

from urllib import request as req

url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F5311%2F2019%2F12%2F10%2F0000012851_001_20191210085008187.jpg&type=a340'
imgName = 'myImg.png'

site = req.urlopen(url)
page = site.read()

#r:read w:write
#t:text(default) b:binary
with open(imgName, "wb") as f:
    f.write(page)
