# 부울형 - 첫글자는 반드시 대문자 True, False, None 여야 한다
from sympy import false

t = True
f = False
n = None    # 다른 언어의  null 값과 유사

# hungry = True
# sleepy = False
# print(type(hungry)) #  python(파이썬)에서는 boolean 이 아닌 bool 이라고 함
# print(not hungry)
#
# print( hungry and sleepy)
# print( hungry or sleepy)
#
# print( hungry & sleepy)
# print( hungry | sleepy)


"""
        자료형         값           부울형
    -----------------------------------------------------
        문자형       "문자"          True
                    ""                     False
        리스트       [1,2,3]         True       
                    []                     False
        튜플         ()                     False
        딕셔너리     {}                     False
        숫자형       0이아닌 숫자     True
                    0                      False
                    None                   False


"""

if('아'):
    print('True') #true
else:
    print('False')

if([]): #문자가 비어있으면 true
    print('True2') #false
else:
    print('False2')

if(0):
    print('True3') #false
else:
    print('False3')

if(-1):
    print('True4') #true
else:
    print('False4')

msg = '행복합시다'
if msg.find('행'): # 0번째 => false
    print('True5') #false
else:
    print('False5')
if msg.find('가'): # 없어서 -1로 치환되어서 => true
    print('True6') #true
else:
    print('False6')
 #s.count('글') : s 문자열에서 '글'이라는 문자 개수 세기

if msg.count('행'): # 문자가 있는지 없는지를 찾는다 (0이상이면 true)
    print('True7')
else:
    print('False7')


'''
1. 3 
2. 2
3. Gachon + n + ' ' +  Human
4.
5.
6.
7.
8.
'''