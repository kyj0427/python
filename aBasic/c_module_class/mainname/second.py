import first  # first 모듈을 가져옴

print('second.py __name__:', __name__)  # __name__ 변수 출력 #자기자신 파일에서는 __main__출력
#first.py __name__: first (자기자신 파일명 출력) -> import해서