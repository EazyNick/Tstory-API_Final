#"파싱" : 텍스트나 데이터를 분석하고 원하는 정보를 추출하는 과정

from getAccessToken import getAccessToken
from getCategory import getcategory
from Write_post import write_post
from Write_Review import write_review
import chatgpt
import BeautifulSoup
# 실행 방법
# getcode 실행 후 현재 파일 실행

code = "" # authorize url 접속 후 나오는 code값 넣어주기.

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 내용 작성

# 제목

# title = "오늘의 Top 5 뉴스입니다." 
# content = BeautifulSoup.html_with_br # 뉴스파싱
# tag = 'Python, 자동화, 뉴스'

# tap 원할시 <pre> /t내용</pre>, 줄바꿈 원할시
# 현재 : 스트링 -> 엔터 기준으로 리스트 나눔 -> 리스트를 줄바꾸며 다시 스트링으로 합침.
# 내용 , # #문자 재배열

title = "하루 10개 영단어 외우기"
content = chatgpt.formatted_rows # 영단어
content_lines = content.split('\n')
content = "<br>".join(content_lines) 
tag = 'Python, 자동화, 영단어' # 태그 설정 ','로 구분
#-----------------------------------------------------------------------------------------------------------------------------------------------------

category = "" # 카테고리 설정, 카테고리 ID 입력
#타임 스탬프 값 (밀리 초 단위로 시간을 작성, 추후 구현)
#published = "645425432"
reviewcontent = '이 글은 자동으로 작성된 글입니다.'

blogname = ''

post_id = 57
 
# content = """테스트 할꺼에요 띄어쓰기가 되나요? 띄어쓰기만 가능
# 줄바꿈도 되나?
# 안됨"""

if __name__ == "__main__":
    token = getAccessToken(code).content.decode('utf-8')
    accessToken = token.replace("access_token=", '')
    print("access_token :", accessToken)

    # get_category = getcategory(token, blogname) # 카테고리 ID 찾을 때 필요.
    # print(get_category)

    post_result = write_post(token, blogname, title, category, tag, content)
    print(post_result)

    # #댓글 작성, 사용자 인식이 안된다고 안됨. 해결 불가
    # post_id = post_result['tistory']['postId']
    # review_result = write_review(token, blogname, post_id, reviewcontent)
    # print(review_result)




# 댓글 작성 기능 테스트 - 안됨. {'tistory': {'status': '412', 'error_message': '댓글 쓰기 중 사용자를 식별할 수 없습니다. '}} 에러 반환
# 고객센터에 문의는 해둠. 해결불가.
# 23.11.16 에 API 고쳐짐.



    

