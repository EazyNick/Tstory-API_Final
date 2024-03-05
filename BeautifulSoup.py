import requests
from bs4 import BeautifulSoup

# 웹 페이지 URL
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"

# HTTP 요청 헤더에 User-Agent 추가
headers = {"User-Agent": user_agent}

# GET 요청 보내기
response = requests.get(url, headers=headers)

#print("응답 값: ", response)

# 웹 페이지 파싱
soup = BeautifulSoup(response.text, "html.parser")

#print("soup :", soup) # 테스트 해봐야함.

# 뉴스 추출
news_titles = soup.find_all("a", class_="sa_text_title")

html_with_br = ""

# for title in news_titles:
#     br_tag1 = soup.new_tag("br")
#     br_tag2 = soup.new_tag('br')
    
#     # title 태그 뒤에 <br> 태그 두 개를 삽입
#     title.insert_after(br_tag2)
#     title.insert_after(br_tag1)

#     html_with_br += str(title) + str(br_tag1) + str(br_tag2)
#     #print(html_with_br)

#24.02.01 날짜꺼
# for title in news_titles:
#     # 현재 타이틀 뒤에 <br> 태그를 추가
#     br_tag1 = soup.new_tag("br")
#     br_tag2 = soup.new_tag('br')

#     # soup 자체에 br을 추기하는 것.
#     #title.insert_after(br_tag1)
#     #title.insert_after(br_tag2)

#     html_with_br += str(title) + str(br_tag1) + str(br_tag2)
#     print(html_with_br)


# print(soup)
# a = BeautifulSoup(html_with_br, "html.parser").prettify()
# print(BeautifulSoup(html_with_br, "html.parser").prettify())

# a = BeautifulSoup(html_with_br, "html.parser").prettify()
# print(BeautifulSoup(html_with_br, "html.parser").prettify())


#추출 과정

# for i in range(5):
#     url = news_titles[i].get("href")
#     # news = str(news_titles[i])
#     # news = news.replace("특정 문구", "")
#     # news += news_titles[i] + " "
#     # news += url + " "
#     print("뉴스 제목:", news_titles[i])
#     print("url :", url)

# print("최종 :", new_title)

