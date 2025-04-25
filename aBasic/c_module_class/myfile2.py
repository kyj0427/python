# myfile2.py


#mymodule이 mypack 패키지 안에 위치할 때
'''
import mypack.mymodule
print('오늘은', mypack.mymodule.get_weather()) #패키지.모듈.함수
'''
'''
#from에 import한 경우 모듈부터 입력가능
from mypack import mymodule 
print('오늘은', mymodule.get_weather())
'''

#별칭 쓰면 별칭만 사용 가능 (별칭에 관행이 있음)
from mypack import mymodule as mm
print('오늘은', mm.get_weather())