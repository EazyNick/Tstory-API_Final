from Write_Review import write_review
from getAccessToken import getAccessToken

#동작이 안된다.
# 에러 메시지 : {'tistory': {'status': '412', 'error_message': '댓글 쓰기 중 사용자를 식별할 수 없습니다. '}}

code = ""

post_id = "157"
token = getAccessToken(code).content.decode('utf-8')
blogname = 'kimsungjun9987'
reviewcontent = 'test'

review_result = write_review(token, blogname, post_id, reviewcontent)
print(review_result)