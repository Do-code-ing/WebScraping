# requests.get(".") 할 때 오류가 나는 이유는
# 해당 사이트에서 정상적이지 않은 접속시도를 차단하는 것
# 라고 보면 될듯
# 그래서 사용하는 것이 user_agent

import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status() # 위 코드랑 같은 함수 사용
with open("nadocoding.html", "w", encoding="utf8") as f: # 받아온 값을 파일로 저장
    f.write(res.text)