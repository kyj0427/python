"""
    전세계날씨제공 API : http://openweathermap.org

    1. 회원가입 : 메뉴 > Sign Up > 사용용도 : Education > 대충가입 (무료는 1번에 60번 호출 가능 )
    2. 개발자모드 : Sign In > API Keys 에서 내가 발급받은 키 (추가 키 가능)
    3. 발급받고 바로 지정 안됨 (시간소요)
"""

# API 키를 지정합니다. 자신의 키로 변경해서 사용해주세요.
apikey = "bHmfI5LKTM-5nyOSyozPwQ"

#위치 설정
nx = "57"
ny = "127"



# url 지정
api = "https://apihub.kma.go.kr/api/typ02/openApi/VilageFcstInfoService_2.0/getUltraSrtNcst"


import requests
import json
import datetime

# 현재 날짜 및 시간 계산

now = datetime.datetime.now()

base_date = now.strftime("%Y%m%d")

base_time = "0600"

# 현재 날짜 및 시간 계산

now = datetime.datetime.now()

base_date = now.strftime("%Y%m%d")

base_time = "0600"



params = {

    'serviceKey': apikey,

    'pageNo': '1',

    'numOfRows': '1000',

    'dataType': 'JSON',

    'base_date': base_date,

    'base_time': base_time,

    'nx': '59',

    'ny': '126'

}

response = requests.get(api, params=params)

# print(response.text)  # 응답 내용 출력

data = response.json()

print(json.dumps(data, indent=4, ensure_ascii=False))


for item in data["response"]["body"]["items"]["item"]:

    if item["category"] == "T1H": # 기온 데이터
     print(f"예보 시간: {item['baseTime']}, 기온: {item['obsrValue']}°C")