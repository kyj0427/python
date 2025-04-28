#Oracle_test.py
'''
 [ 설치 ]

 pip install cs_Oracle

 [ 절차 ]

1) 연결객체 얻어오기
2) SQL 문장
3) cursor 객체 얻어오기
4) SQL 전송
5) cursor 닫기
6) 연결 객체 닫기

'''

import cx_Oracle as oci

# 1) 연결객체 얻어오기
conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
print('연결성공')
# 2) SQL 문장
sql = 'SELECT * FROM emp'
# 3) cursor 객체 얻어오기
cursor = conn.cursor() #변수명을 설정해서 conn를 얻어온다
# 4) SQL 전송
cursor.execute(sql) #파이썬은 기본적으로 excute 를 사용한다

#결과처리
for row in cursor: # 변수명
    #print(row) # tuple 형식 => list 로 출력
    print(row[0],row[1],row[5])
# 5) cursor 닫기
cursor.close()
# 6) 연결 객체 닫기
conn.close()