"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록{}을 대신 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
i = 0;
i2=0.0
i3=""
i4=str()
i5=list()
i6=tuple()
i7=set()
i8=dict()
i9={}
i10=None
# (포인트는) 값이 없거나 0인경우 모두 거짓

a = -1
if a:
    print('True')
else:
    print('False')

a=0
if a:
    print('True')
else:
    print('False')

# 논리연산자와 이용 -------------------------
a = 10
b = -1

if a and b:
    print('True2')
if a or b:
    print('True3')

print(a and b) #-1 //둘다 참이기떄문에 뒤에값 반영
print(a or b)  #10 //뒤에값이 중요하지않다, 앞에 값에서 결정된다.