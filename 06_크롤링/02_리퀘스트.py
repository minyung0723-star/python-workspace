'''
파이썬으로 "브라우저처럼" 서버에 요청을 보내는 도구
pip install requests
'''

import requests

# 네이버 사이트에 "GET 요청" 보내기
# 요청을 보내다.get("특정URL 주소로")
네이버_온_응답 = requests.get("https://www.naver.com")

# status = 200(성공) 404(페이지 없음) 403(접근 권한 없음) 500(회사 서버 로직 오류)
print(네이버_온_응답.status_code)
print(네이버_온_응답.text)