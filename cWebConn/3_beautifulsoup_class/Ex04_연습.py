
from urllib import request as rq
from bs4 import BeautifulSoup

#[1]
'''
url = 'http://www.pythonscraping.com/pages/warandpeace.html'
res = rq.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')

green = soup.select('.green')
for green in green:
    print(green.text)
'''
#[2]
url = 'http://www.pythonscraping.com/pages/page3.html'
res = rq.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')

product = soup.select('.gift td:nth-child(1)' )

price = soup.select('.gift td:nth-child(3)' )

# #tuple
# for t,p in zip(product,price):
#     print(t.text.strip(),p.text.strip())
#


#iterator
#컨프리헨션 스타일
item = [item.text.replace('\n', '') for item in soup.select('.gift > td:nth-child(1)')]
price = [price.text.replace('\n', '') for price in soup.select('tr.gift > td:nth-child(3)')]
array = zip(item, price)
print(*array, sep='\n')


