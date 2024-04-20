from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# ChromeOptions 객체 생성
options = Options()
# 필요한 추가 옵션 설정
# options.add_argument('--headless')  # 브라우저를 헤드리스 모드로 실행
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')  # GPU 하드웨어 가속 비활성화


# Service 객체 생성
s = Service(r'C:\Users\yamish\Desktop\python\crawling\chromedriver-win64\chromedriver.exe')

# Chrome WebDriver 초기화
driver = webdriver.Chrome(service=s, options=options)

driver.implicitly_wait(2)
driver.get('https://www.daum.net')
time.sleep(10)
