from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import pymysql
import requests
import re
import pandas as pd
import folium
from sqlalchemy import create_engine

def clean_address(addr):
    # 괄호 안 내용 제거 (ex: (이동), (신문동) 등)
    addr = re.sub(r"\(.*?\)", "", addr)
    # 불필요한 상세 주소 제거 (지하, 상가, 호 등)
    addr = re.sub(r"[0-9]+호", "", addr)
    addr = re.sub(r"지하\s?[0-9]*층?", "", addr)
    addr = re.sub(r"상가", "", addr)

    return addr.strip()
#  카카오 REST API 키
KAKAO_API_KEY = "fa197b78ef6ea110fc7f3698fb7d470e"

#  주소 → 좌표 변환 함수
def get_coordinates(address):
    url = "https://dapi.kakao.com/v2/local/search/address.json"
    headers = {
        "Authorization": f"KakaoAK {KAKAO_API_KEY}"
    }
    params = {
        "query": address
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        result = response.json()
        if result['documents']:
            x = float(result['documents'][0]['x'])  # 경도
            y = float(result['documents'][0]['y'])  # 위도
            return y, x
    return None, None  # 실패 시 None 반환

# 1.DB 연결
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    port=3306,
    password='admin1234',
    database='basic',
    charset='utf8'
)
cursor = conn.cursor()

# 1. webdriver 객체생성
options = Options()
# 브라우저 꺼짐 방지 코드
options.add_experimental_option("detach", True)
# 불필요한 에러 메세지 제거 코드
# options.add_experimental_option("excludeSwitched",["enable-logging"]);
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)


# 또레오레 > 매장찾기
driver.get('https://www.toreore.com/board/store/board_list.php')

time.sleep(3)

# [배열 형태로 지역 저장]
regions = ["서울특별시", "강원도", "경기도", "경상남도"]

# 0. 도/시 선택
for region in regions:
    driver.find_elements(By.CLASS_NAME, "btn_selected")[0].click()
    time.sleep(3)


# 1. 셀렉트 박스에서 해당 지역 선택

    btns = driver.find_elements(By.CLASS_NAME, "item_btn")
    for btn in btns:
        if btn.text.strip() == region:
            driver.execute_script("arguments[0].click();", btn) # JS 클릭
            break
    time.sleep(2)

    # 2. 검색 버튼 클릭
    search_btn = driver.find_element(By.CLASS_NAME, "btn_search_store")
    driver.execute_script("arguments[0].click();", search_btn)

    # 3. 페이지 로딩 대기
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "store_item"))
    )

    # 4. 파싱
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # 매장 아이템 추출
    store_items = soup.select('.store_item')  # 실제 클래스명

    # 매장명	전화번호	주소
    for store in store_items:
        name_tag = store.select_one('.store_item_name')
        tel_tag = store.select_one('.store_item_tel')
        addr_tag = store.select_one('.store_item_addr')



        # 예외 처리 (혹시 누락된 태그 있을 경우)
        if name_tag is None or tel_tag is None or addr_tag is None:
            continue
        # 텍스트 추출
        store_name = name_tag.text.strip()
        store_tel = tel_tag.text.strip()
        store_addr = addr_tag.text.strip()

        print(f'{store_name} | {store_tel} | {store_addr}')

        # DB에 저장

        cursor.execute(
            "INSERT INTO toreore_store (name, tel, addr) VALUES (%s, %s, %s)",
            (store_name, store_tel, store_addr)
        )

        # 1. 카카오 API로 주소 → 좌표 변환
        cleaned_addr = clean_address(store_addr)
        lat, lng = get_coordinates(cleaned_addr)

        # 2. 좌표가 존재하면 해당 row에 UPDATE
        if lat and lng:
            cursor.execute(
                "UPDATE toreore_store SET lat = %s, lng = %s WHERE name = %s AND addr = %s",
                (lat, lng, store_name, store_addr)
            )
            print(f"  → 위도/경도 저장 완료: {lat}, {lng}")
        else:
            print("  → 좌표 변환 실패")



#DB 저장 및 종료
conn.commit()
cursor.close()
conn.close()

# DB 다시 연결 (SQLAlchemy 사용 → pandas 연동용)
engine = create_engine("mysql+pymysql://root:admin1234@localhost:3306/basic?charset=utf8mb4")

# 위도/경도 데이터 조회
sql = """
SELECT 
  name AS store_name,
  tel AS phone,
  lat,
  lng
FROM toreore_store
WHERE lat IS NOT NULL AND lng IS NOT NULL
"""
df = pd.read_sql(sql, engine)

# 지도 초기 위치: 서울 중심
m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

# 마커 추가
for _, row in df.iterrows():
    popup_html = f"""
        <b>{row['store_name']}</b><br>
        📞 {row['phone']}
    """
    popup = folium.Popup(popup_html, max_width=300)

    folium.Marker(
        location=[row['lat'], row['lng']],
        popup=popup,
        icon=folium.Icon(color='blue', icon='cutlery', prefix='fa')
    ).add_to(m)

# HTML 저장
m.save("또래오래_매장지도.html")
print("📍 지도 시각화 완료: '또래오래_매장지도.html' 저장됨")