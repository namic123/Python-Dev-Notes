# selenium이 제대로 설치되었는지 확인하는 테스트 코드 (주석 처리됨)
# try:
#     from selenium import webdriver
#     print("selenium 정상 설치됨")
# except ImportError as e:
#     print("selenium import 실패:", e)

# Selenium 웹드라이버 모듈 임포트
from selenium import webdriver

# 크롬 웹드라이버 실행에 필요한 서비스 객체와 옵션 객체를 위한 모듈 임포트
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 요소 선택(By) 및 키보드 조작(Keys)을 위한 모듈 임포트
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 웹드라이버 자동 설치 도우미 패키지 (webdriver-manager)
from webdriver_manager.chrome import ChromeDriverManager

# 대기 및 sleep 처리를 위한 time 모듈
import time

# ChromeDriverManager를 이용하여 크롬 드라이버를 자동 설치하고 Service 객체로 초기화
customService = Service(ChromeDriverManager().install())

# 크롬 브라우저의 실행 옵션을 담는 객체 생성 (필요시 headless 등 설정 가능)
customOptions = Options()

# 위에서 정의한 서비스와 옵션을 사용하여 Chrome 브라우저 실행
browser = webdriver.Chrome(service=customService, options=customOptions)

# 접속할 웹 페이지 주소 설정 (네이버 메인 페이지)
URL = 'https://www.naver.com'

# 지정된 URL로 브라우저 접속
browser.get(URL)

# 웹 페이지 내 요소들이 로드될 때까지 최대 10초까지 대기 (암시적 대기)
browser.implicitly_wait(10)

#######################################################
# 네이버 메인 화면 메일 xPath 설정 후, 메일 text 값 획득
temp = browser.find_element(By.XPATH, '//*[@id="shortcutArea"]/ul/li[1]/a/span[2]').text
print(temp)

# 검색창 xpath 설정 후, '크롤링' 이라는 텍스트 입력
browser.find_element(By.XPATH, '//*[@id="query"]').send_keys('크롤링')
time.sleep(3)

# 검색창의 검색 버튼 xpath 설정 후, 클릭 버튼
browser.find_element(By.XPATH, '//*[@id="sform"]/fieldset/button').click()
time.sleep(3)

# 로그인 버튼
# #버튼 클릭
# browser.find_element(By.XPATH, '//*[@id="account"]/div/a').click()

# 동작 확인을 위해 3초 대기 (명시적 대기: 실제 테스트 시 필요에 따라 조정)
time.sleep(3)
