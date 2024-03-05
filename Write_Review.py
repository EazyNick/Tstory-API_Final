import requests

tistory_write_review_url = 'https://www.tistory.com/apis/comment/write?'
secret = 0


def write_review(token, blogname, post_id, reviewcontent):
    data = f'{tistory_write_review_url}{token}&output=json&blogName={blogname}&postId={post_id}&content={reviewcontent}&secret={secret}' 
    return requests.post(data).json() #json 형태로 받아와 print 할 예정