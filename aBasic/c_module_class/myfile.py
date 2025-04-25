# myfile.py
# mymodule을 패키지안으로 옮기기 전
# [1] 모듈 전체를 참조할 때
from c_module_class.mypack import mymodule

#mymodule안에 print가 있어 따로 적지않아도 출력됨 -> mymodule 전체를 읽어들여서 실행
print('오늘의 날씨는', mymodule.get_weather())
print('오늘은', mymodule.get_date(), '요일입니다')
#mymodule에서 if __name__ == '__main__' : 추가하면 외부파일에서 mymodule안 print문이 출력되지 않음

#다른 파일에 들어있는 함수 또는 클래스를

'''
# [2] 별칭 부여
import mymodule as mm

print('오늘의 날씨는', mm.get_weather())
print('오늘은', mm.get_date(), '요일입니다')
'''
'''
# [3] 모듈에서 필요한 부분만 임포트
from mymodule import get_weather
print('오늘의 날씨는', get_weather()) # 함수만 끌어오면 앞에 안붙이고 사용

# print('오늘은', mymodule.get_date(), '요일입니다') # 에러
'''
'''
# [4] 모듈에서 필요한 부분만 임포트하고 별칭 부여
from mymodule import get_weather as gw
print('오늘의 날씨는', gw()) #별칭을 부여하면 원래 이름을 사용하지 못함
'''