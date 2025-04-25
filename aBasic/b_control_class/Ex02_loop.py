
# ------------------------------------------------------
"""

   (2) for문
        for <타켓변수> in 집합객체 :
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
a = 112                  # 숫자형
b = ['1','2','3']        # 리스트
c = '987'                # 문자열 (문자열도 집합으로 취급한다)
d = tuple(b)             # 튜플 (변수)b를 출력
e = dict(k=5, j=6)       # 딕셔너리 (key만 출력) , ex).items() 를사용하면 값도 같이 출력
f = {4,5,6}              # set

for entry in e.items(): # a는 반복이 안되지만 b부터 e까지는 반복된다.
    #print(entry)
    print('키:',entry[0], '값',entry[1]) # key와 value 를 각각 출력할수있다.
else: # for문이 중간에 break 없이 정상 종료되면 실행됨
    print('끝')

#1부터 10까지의 합을 구하기
sum = 0 #변수생성
for i in range(1,11): # 1부터 10까지 (11-1)
    sum += i
print('1부터 10까지의 합:', sum)
print(i)

# 1 부터 10까지의 홀수의 합
sum = 0 #변수생성
for i in range(1,11,2): # 1부터 10까지 (11-1)
    sum += i
print('1부터 10까지의 합:', sum)
print(i)


for a in range(2,10):
    for b in range(1,10):
        print('{0} * {1} ={2}'.format(a,b,a*b))

a = ['x','y','z']
while a:
    data = a.pop() #요소가 비어있으면 무조건 false 취급
    print(data)
    if data == 'y':break;
else: # 조건문이 false인경우에만 출력
    print('데이터가 비었음')



"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
