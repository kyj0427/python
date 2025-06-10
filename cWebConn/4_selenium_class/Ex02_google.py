'''
1. 크롬웹드라이버로 구글 사이트 열기

2. 실제 크롬창에서 '파이썬'라고 검색버튼을 누른다.
    개발자모드(F12)에서 이 부분을 보면
    <input name='q' value='파이썬'~~ >
    그리고 'google검색' 버튼이 type='submit' 인거 확인
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


options = Options()
# 브라우저 꺼짐 방지 코드
options.add_experimental_option("detach", True)
# 불필요한 에러 메세지 제거 코드
# options.add_experimental_option("excludeSwitched",["enable-logging"]);
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(2)







# driver.close()  # 이 코드 없으면 크롬창이 안 닫힘