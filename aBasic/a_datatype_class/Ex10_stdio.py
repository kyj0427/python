"""

stdio : 표준입출력


    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""

'''
name = input('이름을 입력->')
#출력방법 3가지
print('당신은',name,'입니다')
print('당신은 %s 입니다' %name)
print('당신은 {0} 입니다' .format(name))
'''

#-------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력
# age = input('나이를 입력->') #에러발생
# print('나이는', age+1)

'''
age = int(input('나이를 입력->')) #int로 형변환
print('나이는', age+1)
# 23.1 실수 입력 -> 에러발생 invalid literal for int() with base 10: '23.1' 

height = float(input('키를 입력->'))
print('키는', height)
'''

'''
age = eval(input('나이를 입력->')) #int인지 float일지 모를때 eval()함수사용 -> 정수를입력하면 정수, 실수입력하면 실수
print('나이는', age+1)

height = eval(input('키를 입력->'))
print('키는', height)

print('1+2') #문자열
print(eval('1+2')) #eval()함수에 넣으면 3 출력 
'''
#----------------------------------
# 단을 입력받아 구구단을 구하기
dan = int(input('단 입력->'))

for i in range(1,10):
    print('{} * {} = {}'.format(dan,i,dan*i))



#-----------------------------------------
# print() 함수
'''
print('안녕' + '친구') #문자열 더하기 연산 가능
print('안녕' , '친구') #파이썬의 권장 , 컴마찍었을때만 개행이 됨
print('안녕'  '친구') #아무것도 없어도 가능
'''
''' [java]
for (int i=0; i<5; i++) {
    System.out.println(i);
    }

    자바의 코딩과 아래 코딩이 동일
'''
'''
for i in range(0,5): #기본이 향상된 for문
    print(i) #자바의 println과 같은 기능 (개행)

for i in range(5): # 0~(5-1) , 어차피 시작이 0이면 생략함
    print(i, end=',' if i<4 else "") # end를 지정하면 개행이 안됨, if문사용가능 : i가4보다작으면 end=','실행, 그렇지않으면 ""실행
'''
# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3
