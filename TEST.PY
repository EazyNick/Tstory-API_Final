# from bs4 import BeautifulSoup

# html = '''
# <a href="https://n.news.naver.com/mnews/article/629/0000238718?sid=101" class="sh_text_headline nclicks(cls_eco.clsart)">요소수 대란 없다…정부 "차량용 내년 2월분까지 재고 확보"</a>
# '''

# # BeautifulSoup을 사용하여 HTML 파싱
# soup = BeautifulSoup(html, "html.parser")

# # <a> 태그의 href 속성 가져오기
# link_element = soup.find("a", class_="sh_text_headline nclicks(cls_eco.clsart)")
# url = link_element.get("href")

# # URL 출력
# print("URL:", url)



import time
import pyautogui as py

test = 2

while True:
    print(py.position())
    time.sleep(test)
    