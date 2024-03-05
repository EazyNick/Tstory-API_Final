# chat gpt는 보안문제로, BeautifulSoup, 셀레니움으론 접속이 불가하다.print
import pandas as pd

# 하루마다 바꿔줄 값, 글 올리고 바로 바꿔주자.
start = 720
end = 730

# 엑셀 파일 읽기
excel_file = r'D:\Python\Tstory\Assets\English1500.xlsx'  # 엑셀 파일 경로
df = pd.read_excel(excel_file)

#dataframe.iloc[행선택, 열선택]
selected_rows = df.iloc[start:end]

formatted_rows = selected_rows.to_string(index=False)

# 결과 출력
#print(formatted_rows)

# json 변환 과정중에 한글이 깨진다.

# 데이터프레임을 JSON으로 변환
#json_data = df.to_json(orient='records')
# JSON 데이터 출력
#/print(json_data)






#chat gpt 수동이용 해서 답변 하기.
# findandClick(r"C:\User Python\Code\Python\Tstory\Assets\Chrome.png", 3)
# py.moveTo(800, 70)
# time.sleep(1)
# py.click()
# time.sleep(1)
# py.press('backspace')
# time.sleep(1)
# #한글로 되어있으면 한글로 입력하니 영어로 설정 해둬야함.
# py.typewrite("https://openai.com/blog/chatgpt")
# time.sleep(3)
# py.press('enter')
# time.sleep(5)
# findandClick(r"C:\User Python\Code\Python\Tstory\Assets\Try ChatGPT.png", 10)
# py.moveTo(895, 920)
# time.sleep(1)
# py.click()
# time.sleep(1)
# py.typewrite('Tell me 10 conversation words to memorize in a day. Tell me the meaning in Korean. Please exclude the pronunciation symbol') #질문 찾아야함.
# time.sleep(50)

# Po = py.locateOnScreen(r"C:\User Python\Code\Python\Tstory\Assets\code.png", confidence=0.9)
# if(Po):
#     py.click(Po)
#     time.sleep(1)

#현재 마우스 좌표 찾기
# while True:
#     print(py.position())
#     time.sleep(2)