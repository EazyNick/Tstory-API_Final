# 보안상 막힘 셀레니움으로 바로 들어가면 막힘.
# 노가다 해야댐..

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# 웹 드라이버 초기화
driver = webdriver.Chrome()  # Chrome 웹 드라이버 사용
init_url = 'https://openai.com/blog/chatgpt'

# URL에 접근
driver.get(init_url)
time.sleep(400)
print("200딜레이 완료")
# driver.get(url)

# 확인 버튼 클릭 (여기에서 확인 버튼의 선택자를 바꾸세요)
confirm_button = driver.find_element(By.CSS_SELECTOR, '#blog-details-chatgpt > div.ui-hero.theme-dark-green > div.theme-dark-green.pb-\[calc\(2\*var\(--inner-gutter\)\)\] > div > div > div > div.xs\:w-6-cols.md\:w-4-cols.lg\:w-6-cols.md\:pr-40.lg\:pr-44 > ul > li:nth-child(1) > a')
print(confirm_button)
confirm_button.click()          

# URL 복사
time.sleep(2)  # 페이지가 로드되기를 기다리기 위한 대기 시간
url_input = driver.find_element(By.XPATH, '//*[@id="prompt-textarea"]')
url_value = url_input.get_attribute("value")

# URL 출력
print("Copied URL:", url_value)

# 웹 드라이버 종료
driver.quit()