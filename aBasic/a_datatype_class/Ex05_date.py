'''
import datetime #datetime모듈 import
today = datetime.date.today() #datetime 모듈 안 date 클래스의 today() 함수
print('today is ', today)
'''


from datetime import  date #datetime모듈 안 date클래스만 import , 연월일만 가져옴
today = date.today()
print('today is ', today)

#today2 = datetime.date.today() -> 에러. import한 것만 쓸 수 있다

# 년, 월, 일
print('년도', today.year)
print('월', today.month)
print('일', today.day)
print('요일', today.weekday()) # Monday is 0 and Sunday is 6

# 날짜 계산
# from datetime import date #중복해서 선언 가능
# from datetime import timedelta
from datetime import date, timedelta #같이쓰기 가능
print('어제 : ', today + timedelta(days=-1))
print('일주일 전 : ', today + timedelta(days=-7))
print('일주일 후 : ', today + timedelta(weeks=+1))
# print('한달 후 : ', today + timedelta(month=1) ) ->에러발생 : 달 계산 불가능

from dateutil.relativedelta import relativedelta #relativedelta : 상대적
print('한달 후 : ', today + relativedelta(month=1)) # 달 계산 가능

# 날짜를 문자열형식으로 변환 => strftime() 이용 (통신의 기본은 문자열, 날짜로 변환할 일이 많음)
# import datetime #연월일 시분초까지 가져옴
# today = datetime.datetime.today()

# 위와 같은 코딩
from datetime import datetime
today = datetime.today()
print(today)

print(today.strftime('%m/%d/%Y')) #미국형식
print(today.strftime('%Y년 %m월 %d일 %H시 %M분')) #한국형식

# 문자열을 날짜형식으로 변환 => strptime() 이용
naljja = '2029-02-22 12:30:22'
print(type(naljja)) #<class 'str'>

mydate = datetime.strptime(naljja, '%Y-%m-%d %H:%M:%S')
print(type(mydate)) #<class 'datetime.datetime'>