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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
# 명시적 대기 객체 설정
wait = WebDriverWait(browser, 10)

# 접속할 웹 페이지 주소 설정 (네이버 메인 페이지)
URL = 'https://www.naver.com'

# 지정된 URL로 브라우저 접속
browser.get(URL)

# 웹 페이지 내 요소들이 로드될 때까지 최대 10초까지 대기 (암시적 대기)
browser.implicitly_wait(5)

#######################################################
# 네이버 메인 화면 메일 xPath 설정 후, 메일 text 값 획득
temp = browser.find_element(By.XPATH, '//*[@id="shortcutArea"]/ul/li[1]/a/span[2]').text
print(temp)

# 검색창 xpath 설정 후, '크롤링' 이라는 텍스트 입력
browser.find_element(By.XPATH, '//*[@id="query"]').send_keys('박재형 바보')
time.sleep(2)

# 검색창의 검색 버튼 xpath 설정 후, 클릭 버튼
browser.find_element(By.XPATH, '//*[@id="sform"]/fieldset/button').click()
time.sleep(2)

browser.find_element(By.XPATH, '//*[@id="header_wrap"]/div/div[1]/div[1]/div/h1/a').click()
time.sleep(2)

# 검색창에 검색어 입력 및 검색
try:
    search_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="query"]')))
    search_input.send_keys('증시 주식 급상승 종목 데이터 가져오기')
    time.sleep(3)

    search_button = browser.find_element(By.XPATH, '//*[@id="right-content-area"]/div/div[5]/div/div[2]/div[2]/ul/li[1]/a')
    search_button.click()
    time.sleep(3)
except Exception as e:
    print("검색 중 오류 발생:", e)

# 새 탭 전환이 필요한 경우 처리
if len(browser.window_handles) > 1:
    browser.switch_to.window(browser.window_handles[-1])

# 주식 데이터 수집
try:
    print("주식 데이터 수집 시작!")

    tmpTitle = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="middle"]/div[1]/div[1]/h2/a'))).text
    tmp1 = browser.find_element(By.XPATH, '//*[@id="rate_info_nxt"]/table/tbody/tr[1]/td[1]/span').text
    tmp2 = browser.find_element(By.XPATH, '//*[@id="rate_info_nxt"]/table/tbody/tr[1]/td[1]/em/span[1]').text
    tmp3 = browser.find_element(By.XPATH, '//*[@id="rate_info_nxt"]/table/tbody/tr[2]/td[1]/span').text
    tmp4 = browser.find_element(By.XPATH, '//*[@id="rate_info_nxt"]/table/tbody/tr[2]/td[1]/em/span[1]').text
    tmp5 = browser.find_element(By.XPATH, '//*[@id="rate_info_nxt"]/table/tbody/tr[1]/td[3]/span').text
    tmp6 = browser.find_element(By.XPATH, '//*[@id="rate_info_nxt"]/table/tbody/tr[1]/td[3]/em/span[1]').text
    tmp7 = browser.find_element(By.XPATH, '//*[@id="rate_info_nxt"]/table/tbody/tr[2]/td[3]/span[1]').text
    tmp8 = browser.find_element(By.XPATH, '//*[@id="rate_info_nxt"]/table/tbody/tr[2]/td[3]/em/span[1]').text

    print("✅ 현재 수집한 주식 정보:")
    print("제목:", tmpTitle)
    print("현재가:", tmp1, tmp2)
    print("전일가:", tmp3, tmp4)
    print("고가:", tmp5, tmp6)
    print("저가:", tmp7, tmp8)

except Exception as e:
    print("❌ 주식 데이터 수집 중 오류:", e)

time.sleep(3)
browser.quit()