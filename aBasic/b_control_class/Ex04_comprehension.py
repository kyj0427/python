"""
    @ 컴프리핸션 (comprehension)
    ` 하나 이상의 이터레이터로부터 파이썬 자료구조를 만드는 컴팩트한 방법
    ` 비교적 간단한 구문으로 반복문과 조건 테스트를 결합

    * 리스트 컨프리핸션
        [ 표현식 for 항목 in 순회가능객체 ]
        [ 표현식 for 항목 in 순회가능객체 if 조건 ]

    * 딕셔러리 컨프리핸션
        { 키_표현식: 값_표현식 for 표현식 in 순회가능객체 }

    * 셋 컨프리핸션
        { 표현식 for 표현식 in 순회가능객체 }

"""


# 컨프리핸션 사용하지 않은 리스트 생성
'''
alist = []
alist.append(1)
alist.append(2)
alist.append(3)
alist.append(4)
alist.append(5)
alist.append(6)
print(alist)

alist = []
for n in range(1,7):
    alist.append(n)
print(alist)

alist = list(range(1,7))
print(alist)
'''
#동일한 결과 출력 (여기까지 기존 문법)

#------------------------------------------------
# 리스트 컨프리핸션
blist = [n for n in range(1,7)] #변수 n에 1~6까지 뽑아서 list에 담음 (위와 같은 결과값 출력)
print(blist)

blist = [n-1 for n in range(1,7)] #컨프리핸션 사용 이유 : 반복문 구동 후 뽑은 값들로 연산이 가능, 연산 후 list에 담음
print(blist)

blist = [n**2 for n in range(1,7)]
print(blist)

blist = [n**2 for n in range(1,7) if n%2 == 1] # if문 가능
print(blist)
#for : 1~6까지의 값을 변수 n에 저장 -> if : n을 2로 나눈 나머지가 1인 값으로 걸러냄, n을 2의 자승한 값을 list에 담음

#for문부터 읽고 if문 거쳐서 나온 값을 연산해서 blist에 담는다

#컴프리핸션이 없는 리스트 생성
clist = []
for r in range(1,4) : # 1, 2, 3
    for c in range(1,3): # 1, 2
        clist.append((r,c)) #소괄호로 묶음 -> tuple
print(clist) #[(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]

# 컴프리핸션 사용 (같은코딩)
clist = [ (r,c) for r in range(1,4) for c in range(1,3)]
print(clist) #[(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]
#------------------------------------------------
# 셋 컨프리핸션
data = (1,2,3,2,1,5,6) #tuple

dlist = [ n-1 for n in data] #list
print(dlist) #[0, 1, 2, 1, 0, 4, 5]

dset = {n-1 for n in data} #set
print(dset)  #{0, 1, 2, 4, 5} => 중복이 없음

#-------------------------------------------
# 딕셔러니 컨프리핸션
datas = (2,3,4)
adic = { x:x**2 for x in datas} # datas에서 뽑은 값을 x에 하나씩 넣고 key: x, value x**2
print(adic) #{2: 4, 3: 9, 4: 16}

word = 'LOVE LOL'
wcnt = { letter:word.count(letter) for letter in word}
#word에서 하나씩 뽑아 letter에 넣고 key : letter, value : word에서 letter의 갯수(ex.l 은 word에서 3개)
print(wcnt) #{'L': 3, 'O': 2, 'V': 1, 'E': 1, ' ': 1} : l을 3번 센다

wcnt = { letter:word.count(letter) for letter in set(word)}
#set을 안쓰면 L같이 중복되는 값을 계속 덮어씀 -> dictionary는 중복값을 덮어씀: l을 한번만 센다
print(wcnt) #{'E': 1, 'V': 1, ' ': 1, 'L': 3, 'O': 2}







#------------------------------------------------
# 프로젝트할 때 팀구호
우리의결의= """취하고싶으면달려라
맡은업무는반드시마치자
노력없는성과는없다
구글신과함께공부하자"""

result = [ j[i*2] for i, j in enumerate(우리의결의.splitlines())] 
print(result) # ['취', '업', '성', '공']


''' 
enumerate() : 각 요소와 인덱스를 같이 지정
 0 취하고싶으면달려라
 1 맡은업무는반드시마치자
 2 노력없는성과는없다
 3 구글신과함께공부하자
i가 숫자, j가 문장 
j에서 [i*2]번째 위치 
0 : 취
1 : 업
2 : 성
3 : 공
'''











# -------------------------------------------------
# 프로젝트할 때 팀구호
#우리의결의= """취하고싶으면달려라
#맡은업무는반드시마치자
#노력없는성과는없다
#구글신과함께공부하자
#"""
#result = [ j[i*2] for i, j in enumerate(우리의결의.split('\n')]
#print(result)