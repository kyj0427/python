"""
    파일을 다운받고 저장하는 함수

     [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
"""
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

#parse => 어떤것을 쪼개서 구조를 파악해줌
def download_file(url):
    p = parse.urlparse(url)
    print('1>', p)
    savepath = "./" +p.netloc + p.path
    print('2>', savepath)

    #정규화
    #savepath 경로가 / 로 끝나면
    if re.search('/$', savepath):
        savepath += 'index.html'
        print('3>', savepath)

    # 내폴더에 파일 존재하면 다운받을 필요없음
    if os.path.exists(savepath): return savepath

    # 다운받을 위치 폴더 지정
    savedir = os.path.dirname(savepath)
    if not os.path.exists(savedir):
        os.makedirs(savedir, exist_ok=True)

    # 다운받기
    try:
        request.urlretrieve(url, savepath)
        time.sleep(2)
        return savepath

    except:
        print('fall download:', url)
        return None

if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'
    result = download_file(url)
    print(result)



