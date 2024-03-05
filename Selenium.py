from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 웹 드라이버 초기화 (예: Chrome 드라이버)
XPATH_LIST = {
    '//*[@id="main_content"]/div/div[2]/div[1]/ul/li[1]/div[2]/a', 
    '//*[@id="main_content"]/div/div[2]/div[1]/ul/li[2]/div[2]/a',
    '//*[@id="main_content"]/div/div[2]/div[1]/ul/li[3]/div[2]/a',
    '//*[@id="main_content"]/div/div[2]/div[1]/ul/li[4]/div[2]/a',
    '//*[@id="main_content"]/div/div[2]/div[1]/ul/li[5]/div[2]/a',
    }


# 웹 페이지 열기
for i in XPATH_LIST:
    element2 = ""
    driver = webdriver.Chrome()
    driver.get("https://news.naver.com")
    time.sleep(1)
    element1 = driver.find_element(By.XPATH, '/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[3]/a/span')
    element1.click()
    time.sleep(1)
    # 웹 페이지에서 데이터를 가져오기 (CSS 선택자를 사용)
    element2 = driver.find_element(By.XPATH, i)
    element2.click()
    time.sleep(1)
    driver.quit()
    time.sleep(3)

