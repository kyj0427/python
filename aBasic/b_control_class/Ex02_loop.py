
# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 : #(향상된 for문 위주로 사용)
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

"""
a = 112                  # 숫자형 (집합이아님)
b = ['1','2','3']        # 리스트
c = '987'                # 문자열 (집합으로 취급)
d = tuple(b)             # 튜플 (변수 b)
e = dict(k=5, j=6)       # 딕셔너리 (key만 출력) key-value를 가져오려면 e.itmes()
f = {4,5,6}              # set


for entry in e.items(): # a는 반복이 안되지만 b부터 e까지는 반복된다.
    # print(entry) #dictionary출력시 tuple로 출력됨
    print('키:',entry[0],'값:',entry[1]) #tuple은 index가 있어 따로 따로 처리 가능
   # a : 'int' object is not iterable
else: #조건문에 위배될 때 나오는 else
    print('끝')

sum = 0
for i in range(1,11): #1부터 10까지 #for문의 i 변수 : java=지역변수, python=전역변수 (언어별로 다르다)
    sum += i
print('1부터 10까지의 합:', sum)
print(i)

# 1부터 10까지의 홀수의 합
sum = 0
for i in range(1,11,2): #1부터 10까지 2씩 건너뜀
    sum += i
print('1부터 10까지의 홀수의 합:', sum)






"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""

for i in range(2,10):
    print('{}단'.format(i))
    for j in range(1,10):
        # print(i,'*',j,'=',i*j)
        print('{} * {} = {}'.format(i,j,i*j))

a = ['x','y','z']
while a: #a내용이 있어 무조건 True
    data = a.pop() #요소를 하나씩 빼서 x까지 뺏을 때 False가 됨
    print(data)
    if data == 'y': break #data가 y에 오면 break => else에 걸리지 않음
else:
    print('데이터가 비었음')