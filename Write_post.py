import requests

tistory_write_url = 'https://www.tistory.com/apis/post/write?'
visibility = 3 # visibility: 발행상태 (0: 비공개 - 기본값, 1: 보호, 3: 발행)

def write_post(token, blogname, title, category, tag, content):
    #write tistory post
    #내용을 맨뒤에 둬야 카테고리, 태그 등이 입력됨
    data = f'{tistory_write_url}&output=json&{token}&blogName={blogname}&title={title}&visibility={visibility}&category={category}&tag={tag}&content={content}' 
    
    response = requests.post(data)

    if response.status_code == 200:
        try:
            requests.post(data).json()
        except ValueError:
            # JSON 형식이 아닌 경우 처리
            print("응답이 JSON 형식이 아닙니다:", response.text)
    else:
        print("요청이 실패했습니다. 상태 코드:", response.status_code)