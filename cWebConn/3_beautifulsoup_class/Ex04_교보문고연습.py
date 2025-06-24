'''
 [과제] 교보문고에서 파이썬 책 검색하여
    - csv 파일로 저장
    - mysql 테이블에 저장
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup

# 교보문고 > '파이썬' 검색 > 국내도서
html = urlopen("https://search.kyobobook.co.kr/search?keyword=%ED%8C%8C%EC%9D%B4%EC%8D%AC&gbCode=TOT&target=total")

soup = BeautifulSoup(html, 'html.parser')

book_items = soup.select('.prod_item')  # 실제 클래스명

for book in book_items:
    title_tag = book.select_one('span[id^=cmdtName_]')
    author_tags = book.select('a.author')

    if not title_tag:
        continue

    title = title_tag.text.strip()
    authors = [a.text.strip() for a in author_tags]

    print(f'{title} : {", ".join(authors)}')




