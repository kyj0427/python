"""
    [ 함수 ]

     - 반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다
     - 역할별 구문을 작성한다

    #defined 약자 def
     def 함수명(매개변수):
        수행할 문장들
"""

# (0) 인자도 리턴값도 없는 함수
def func():
    print('inside func')
    #return '리턴값'

func() #함수 부르고 끝 (저장하지 않음)

result = func() #함수부르고 결과를 받는다 (return값)
print(result) #return값 없으면 None

# (1) 리턴값이 여러개 있는 함수(***) python에만 있음 --> 여러개의 리턴값을 하나의 튜플로 만들어서 리턴
def func(arg):
    return arg+5, arg-5 #tuple로 만들어 리턴 / (arg+5, arg-5) 소괄호 생략

result = func(10) #arg가 10을 받아서 5를 더해 저장, -5해서 저장
print(result) # (15, 5)

x, y = func(10) #요소분해 (여러개의 집합을 변수 여러개에 저장)
print(x+y) # 20 -> 연산가능

# (2) 위치인자 (positional argument)
def func(greeting, name):
    print(greeting, '!!!', name, '님')

#파이참이 자동으로 함수의 인자값이 파라미터로 들어간다고 알림
func('하이', '박길동')  #위치에 따라 순서대로 들어감
func('김길동','안녕')

# (3) 키워드인자 (keyword argument) , 인자가 여러개 일 때 순서 맞추기 힘들 때 사용
func(name='이길동',greeting='헬로우') #이름을 명확하게 주면 순서 상관없이 지정한 인자로 들어감(순서바뀌어도 가능)

# (4) 매개변수의 갯수와 기본값
def func(greeting, name='아무개'):
    print(greeting, '!!!', name, '님')

func('최길동')
#java :  컴파일 에러, js : '최길동' ,undefined , python :  func() missing 1 required positional argument: 'name'
#인자에 기본값을 설정 , 기본값이 없으면 에러

def func(a, b, c=100):
    return a*2+b+c

print(func(1,2,3))  #7
print(func(10,20))     #140
print(func(c=1, a=2, b=3))   #8


'''
#----------------------------------------------------------------
# (5) 위치 인자 모으기 (*)

첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다 -> a, b, c=0
그러나 네번째 인자부터는 정확히 모른다면? -> *args 사용 

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다
'''
def func(a,b,c=0, *args):
    sum = a + b + c
    for i in args: #args는 tuple -> 반복문 가능
        sum += i
    return sum

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))

#----------------------------------------------------------------
# (6) 키워드 인자 모으기 **kwargs : dictionary로 들어옴
def func(a,b,c=0, *args, **kwargs):
    sum = a + b + c
    for i in args: #args는 tuple -> 반복문 가능
        sum += i

    for k in kwargs: #kwargs : dictionary -> 반복문 가능
        sum += kwargs[k]
    return sum

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, kor=10, eng=20, math=30))
print(func(4, 5, 6,  java=11, python=22))


