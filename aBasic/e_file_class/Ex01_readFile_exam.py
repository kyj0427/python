""" [연습]
    함수 정의 : count_words
    인자 : filename

    인자로 받은 파일명을 open 하여 파일을 읽어서 단어를 수를 출력한다.
    존재하지 않는 파일명으로 예외가 발생해도 아무런 일을 하지 않는다
"""
def count_words(filename):
    fname = './data/' + filename
    try:
        with open(fname,'r',encoding='utf-8') as f:
            contents = f.read()
            words = contents.split()
            num = len(words)
    except Exception as e:
        pass  # pass 대신 완성
    else:
        print('파일명:',fname,'/ 총 단어수:',num)

# 존재하지 않는 파일명도 있음
filenames = ['sample.xml', 'xxxx.xxx', 'temp.json']
for filename in filenames:
    count_words(filename)


