import requests

url = "https://www.tistory.com/oauth/access_token?"
client_id = "" 
client_secret = ""
redirect_uri = ""
grant_type="authorization_code" # authorization_code 고정

def getAccessToken(code): # 토큰 받아오기
    data = url
    data += "client_id="+client_id+"&"
    data += "client_secret="+client_secret+"&"
    data += "redirect_uri="+redirect_uri+"&"
    data += "code="+code+"&"
    data += "grant_type="+grant_type
    print("data =", data)
    return  requests.get(data)