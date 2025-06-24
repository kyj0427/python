from bs4 import BeautifulSoup
from urllib import request as rq
from urllib import parse
import os

from setuptools.command.bdist_egg import safety_flags

#[3]
url = 'https://wikidocs.net/'

res = rq.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')
#[3-1] 책제목 : xxxxx          저자 : oooooo

title = soup.select('.media-heading > .book-subject')
#print(title)

writer = soup.select('.book-detail .menu_link')
#print(writer)

# 1번 for t,p in zip(title,writer):
    #print('책제목:', t.text.strip(), '-- 저자:',p.text.strip())
# 2번
for item in zip(title,writer):
    print('책제목 : {}, 저자 : {}'.format(item[0].text, item[1].text))
# 3번 리스트 컴프리헨션으로 책 정보 리스트 생성
'''book_list = ['책제목 : {}, 저자 : {}'.format(t.text.strip(), w.text.strip()) for t, w in zip(title, writer)]

for book in book_list:
    print(book)'''

images = soup.select('.book-image-box .book-image')
# print(images)
# python에서 True는 첫글자 대문자
os.makedirs('wikiImages', exist_ok=True) #'wikiImages' 라는 이름의 파일 자동생성

'''for image in images:
    img = image.attrs['src']
    imgPath = parse.urljoin(url,img)
    print(imgPath)
'''

for image, title in zip(images,title):
    img = image.attrs['src']
    imgPath = parse.urljoin(url,img)
    print(title.text, '->',imgPath)

    fname = title.text
    fname = fname.replace('<','')
    fname = fname.replace('>','')
    fname = fname.replace(':','')

    # 이미지경로에 한글경우 처리
    # parse.quote_plus(imgPath, safe="://")
    filename = './wikiImages/{}.png'.format(fname)

    try:
        rq.urlretrieve(imgPath, filename)
    except UnicodeEncodeError:
        result = parse.quote_plus(imgPath,safe="://")
        rq.urlretrieve(result, filename)