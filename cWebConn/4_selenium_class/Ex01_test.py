"""
 간단하게 크롬 브라우저를 실행하여 페이지 열기
"""

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
driver = webdriver.Chrome(options=options) #접근이나 인식하기위해서 필요한것

driver.implicitly_wait(3)
"""
driver.implicitly_wait(3) :
    Selenium은 기본적으로 웹 자원들이 모두 로드될때까지 기다려주지만, 
    모든 자원이 로드될때 까지 기다리게 하는 시간을 
    직접 implicitly_wait을 통해 지정할 수 있다.
"""


# 2. 페이지 접근
driver.get('http://www.naver.com')

# 3. 화면을 캡처해서 저장하기
driver.save_screenshot("MyPage.png")


# 하고 나서 다시 닫는거 보여줌
# driver.close()