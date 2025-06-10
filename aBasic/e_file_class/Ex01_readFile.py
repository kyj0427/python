"""
#파일처리가 주요 임무이다.

@ 파일 읽고 쓰기
    - 파일을 읽고 쓰기 전에 파일을 열어야 한다
    - fileObj = open ( filename, mode )
            mode 첫번째 글자 - 작업 표시
            r(read)  : 파일 읽기
            w(write) : 파일 쓰기 ( 파일이 없으면 생성하고 파일이 있으면 덮어쓴다 ) =>주로 사용함
            x(write) : 파일 쓰기 ( 파일이 없을 때만 생성하고 쓴다 )
            a(append) : 파일 추가 ( 파일이 있으면 파일의 끝에서부터 추가하여 쓴다 )

            mode 두번째 글자 - 파일 타입
            t : 텍스트(text) 타입 ( 기본값 )
            b : 이진(binary) 타입
            두번째 글자가 없으면 텍스트 타입이다.

            encoding='utf-8' : 한글

    - 파일을 열고 사용 후에는 반드시 닫아야 한다
"""
'''
try:
    f = open('./data/data.txt','r',encoding='utf-8')
except FileNotFoundError as e: #예외가 발생했을때
    print('파일을 찾을 수 없습니다',e)
else: #예외가 발생하지 않았을때 , 파이썬은 자바와 다르게 else 구문을 자주사용함
    while True:
        line = f.readline() # 한줄씩 읽어서 line 이라는 변수에 담음
        if not line: #파이썬은 변수처리가 가능, line에 내용이 있으면 true 없으면 false
            break #한줄인 경우에는 break 한줄에 붙혀서 가능
        print(line, end='')

    f.close()
# No such file or directory: './data/data.txt'
print('\n\n종료')
'''

'''
f = open('./data/data.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()
    if not line: break
    print(line, end='')
#파이썬에서 try 구문은 필수가아님 
f.close()
'''
'''
# with를 이용하여 자동으로 파일 닫기
# 위 코드과 동일
with open('./data/data.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline() 
        if not line: break
        print(line, end='')
'''
# readline 은 한줄 씩 읽는다
# read 는 통으로 읽는다
# split=> 공백을 중심으로 단어를 쪼개줌
filename = './data/data.txt'
with open(filename,'r',encoding='utf-8')as f:
    contents = f.read()
    print(contents)
    words = contents.split()
    print(words)
    num = len(words) #list 에서 개수를 알고싶을때 사용 =>len

print('파일명',filename,'/ 총 단어수:', num)






