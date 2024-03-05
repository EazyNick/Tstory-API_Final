import requests

def getcategory(token, blogname):
    category_url = f'https://www.tistory.com/apis/category/list?{token}&output=json&blogName={blogname}'
    return requests.get(category_url).json()