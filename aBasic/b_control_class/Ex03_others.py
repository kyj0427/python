msg = '행복해'            # 문자열
li = ['a','b','c']       # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = {'k': 5, 'j': 6, 'l':7 }    # 딕셔너리

# [1] unpacking : 요소분해
'''

'''
a,b,c = msg
print(a)
print(b)
print(c)

a,b,c = li
print(a)
print(b)
print(c)

a,b,c = tpl
print(a)
print(b)
print(c)

a,b,c = di
print(a)
print(b)
print(c)

# [2] enumerate() : 각 요소와 인덱스를 같이 지정해주는 함수
user_list = ['개발자','코더','전문가','분석가']

for value in user_list:
    print(value)

for idx, value in enumerate(user_list): #인덱스와 같이 tuple 형식으로 출력
    print('순서', idx, '값',value)

# [3] zip()
days = ['월','화','수']
doit = ['잠자기','공부','밥먹기','놀기']

print(zip(days,doit)) #객체라고 인식하여 출력
print(list(zip(days,doit))) # 서로다른것을 index끼리 tuple 형식으로 묶어줌
print(dict(zip(days,doit))) # index 끼리 묶어서 key,value로 보여줌

for data in zip(days,doit):
    print(data)
for yoil, halil in zip(days,doit):
    print(yoil,'요일에',halil)