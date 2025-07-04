"""

하지말자 -> 어차피 보안문자로 안됨

네이버 로그인 페이지를 실행하기
    크롬에서 네이버 로그인 페이지를 개발자모드에서 확인하여
    로그인 폼의 아이디와 비밀번호 입력 name 확인
    아이디 : id
    비밀번호 : pw
"""
from re import search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 0. 네이버 로그인 정보
myID = '김용재'
myPW = '8638'

# 1. webdriver 객체생성
options = Options()
# 브라우저 꺼짐 방지 코드
options.add_experimental_option("detach", True)
# 불필요한 에러 메세지 제거 코드
# options.add_experimental_option("excludeSwitched",["enable-logging"]);
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(2) #  자원로드될 때까지 3초 기다림

# atosoft 로그인 하기
driver.get('https://ictedu.atosoft.net/worknet/SLogin.asp')
#아이디 id , 비번 pw
# driver.find_element(By.NAME,'id').send_keys(myID)
# driver.find_element(By.NAME, 'pw').send_keys(myPW)
#
# driver.find_element(By.ID,'log.login').click()

driver.find_element(By.ID,'search').send_keys(myID)

driver.find_element(By.ID,'ui-id-1').click()

driver.find_element(By.ID,'strLoginPwd').send_keys(myPW)

driver.find_element(By.CLASS_NAME,'full-width').click()