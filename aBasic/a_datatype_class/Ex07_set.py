# -----------------------------------------------
#  SET(집합)
#       - 집합에 관련된 자료형
#       - 순서(index)를 지정하지 않는다
#       - 중복을 허용하지 않는다 (**중요**)
#       - { }

s = {}                  # 빈 집합을 생성
s = set()               # 빈 집합을 생성
s = set([1,2,3,1,1])
print(s)

b = { 3,4,5,6,3,4,7 }

#print(s[0]) # 우리가 많이 하는 실수
print(s.intersection(b)) # 교집합
print(s.union()) #합집합

print(s.union(b))
print(s&b) # 교 3
print(s|b) # 합 1234567

#차집합
print(s - b) # 1 2
print(b - s) # 4567