
# [추가] 함수도 객체이다
def case1():
    print('case-1')

def case2():
    print('case-2')

def case3():
    print('case-3')


dic = {'f1': case1, 'f2': case2, 'f3': case3}
# print(dic['f1']) #dic의 f1값의 value -> case1 , case1 함수객체가 들어감 #<function case1 at 0x00000213DFB9A2A0>
case1()     #원래 함수 부르는 방식
dic['f1']() #case1함수를 딕셔너리에 넣어도 호출가능
#---------------------------------------
# 글로벌 변수와 지역변수

# (1)
temp = '글로벌' #글로벌 변수

def func():
    # print('0>', temp)
    # java : 글로벌, js : undefined(hoisting으로 변수를 감지하지만 뒤에서 선언되어 undefined)
    # python : 에러 (cannot access local variable 'temp' where it is not associated with a value)
    # 무조건 변수는 앞에다 쓰자

    temp = '지역' #지역변수
    print('1>', temp) # 지역

func()
print('2>', temp)   #글로벌


# (2)
temp = '글로벌' #글로벌 변수

def func():
    # print('0>', temp)
    global temp     # 지역변수로 만들지않고 글로벌 변수를 참조
    temp = '지역'    #'글로벌'에서 '지역'으로 변경
    print('1>', temp) # 지역

func()
print('2>', temp)   # 지역

'''
#----------------------------------------------
# 람다함수 - 한번 사용하고 버리는 함수
# 파이션에서는 람다함수를 한 줄로 작성???

    파이썬 3.x부터는 람다를 권장하지 않는다고.
    몇몇 개발자들이 람다함수 사용시 직관적이지 않다는 이유라는데
    
    종종 사용됨
    읽을 줄만 알면 된다 
'''
'''
# 일반함수
def f(x,y):
    return x*y
print(f(3,2))

# 람다함수
f = lambda x, y : x*y
print(f(3,2))

'''
# 자바스크립트에서 화살표  (x,y) => x*y


#-----------------------------------------------------------
"""  맵리듀스
    (1) map()
         ` 연속 데이터를 저장하는 시퀀스 자료형에서 요소마다 같은 기능을 적용할 때 사용
         ` 형식 : map(함수명, 리스트형식의 입력값)
         ` 파이썬 3.x에서는 list(map(calc, ex)) 반드시 list를 붙여야 리스트 형식으로 반환된다
           파이썬 2.x에서는 list 없이도 리스트 형식으로 반환
    (2) reduce()
         ` 리스트 같은 시퀀스 자료형에 차례대로 함수를 적용하여 모든 값을 통합하는 함수    
    
    파이썬 2.x에서는 많이 사용하던 함수이지만, 최근 문법의 복잡성으로 권장하지 않는 추세란다.
"""

def calc(x):
    return x*2

data = [1,2,3,4,5]

res = map(calc, data)
print(res) # <map object at 0x000001517C049D20>

res = list(map(calc, data)) #calc함수를 사용하는데 data(집합)에서 하나씩 꺼내서 x에 넣어줌
print(res) # [2, 4, 6, 8, 10]

from functools import reduce #import 필요
def f(x,y):
    return x*y

data = [1,2,3,4,5] # 1,2가 들어감 return 2 / return값 2와 3이 들어가 return 6 / 6, 4 들어가 24 / 24, 5 들어가 120
print(reduce(f,data)) #120


