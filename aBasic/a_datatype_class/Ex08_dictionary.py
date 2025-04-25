"""
    [ dictionary 형 ]
 #제일 헷갈릴 수 있다
    1- 키와 값으로 구성 ( 자바의 map 와 유사 )
    2- 저장된 자료의 순서는 의미 없음
    3- 중괄호 {} 사용
    4- 변경 가능

    ` 사전.keys() : key만 추출 (임의의 순서)
    ` 사전.values() : value만 추출 (임의의 순서)
    ` 사전.items() : key와 value를 튜플로 추출 (임의의 순서)
"""

print('--------- 1. 딕셔너리 요소 --------------- ')
dt = {1:'one', 2:'two', '3':'three'}
print(dt)
print(dt[1]) #dt의 키값이 1인 문자를 출력
print(dt['3']) # key값이 '3' => 데이터타입 맞춰야한다

dt = {1:'one', 2:'two', '3':'three', 1:'first'}
print(dt) #key값이 중복되면 덮어진다
dt = {1:'one', 2:'two', '3':'three', 3:'third'}
print(dt) #key값이 다르기 떄문에 들어가진다

# 키는 숫자와 문자 그리고 튜플이여야 한다. 즉 리스트는 안된다.
# 리스트의  값이 변경 가능하다. 그러나 키값을 변경하면 안되므로 리스트는 안된다
dt2 = {1:'one', 2:'two', (3,4):'turple'}
print(dt2)
print(dt2[(3,4)]) # key 값이 한 덩어리인(3,4) =>튜플

print('--------- 2. 딕셔너리 추가 및 수정  --------------- ')
# 딕셔너리에 값 추가 및 수정
#추가 : 존재하지않는 key값으로 설정
dt2['korea'] = '한국'
print(dt2)
#수정 : 존재하는 key값을 입력후 수정
dt2['korea'] = '서울'
print(dt2)
# 여러개 추가할 때
dt2.update({5:'홍',6:"김"})
print(dt2)

print('--------- 3. Key로 Value값 찾기  --------------- ')
dt2 = {1:'one', 2:'two', (3,4):'turple'}
#print(dt2[3]) --> key에러 발생
print(dt2[2])

print(dt2.get(2)) # get을 이용하여 값을 찾을수있다(error 안남)
print(dt2.get(3))
print(dt2.get(3,'없음'))

# Key와 Value만 따로 검색
