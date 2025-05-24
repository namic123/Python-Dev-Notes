# import ㅔㅌ스트
# try:
#     from selenium import webdriver
#     print("✅ selenium 정상 설치됨")
# except ImportError as e:
#     print("❌ selenium import 실패:", e)

#셀레늄 웹드라이버
from selenium import webdriver

#웹드라이버 객체 생성시 수반될 서비스나 옵션
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#선택자 및 키보드 입력
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

############################################
from webdriver_manager.chrome import ChromeDriverManager

import time

customService = Service(ChromeDriverManager().install())
customOptions = Options()

browser = webdriver.Chrome(service=customService, options=customOptions)

############################################

URL = 'https://www.naver.com'

browser.get(URL)
# 로딩 대기를 위해 10초 wait
browser.implicitly_wait(10)

time.sleep(3)