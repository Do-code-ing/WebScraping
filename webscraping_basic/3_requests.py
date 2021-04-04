import requests
res = requests.get("http://google.com") # 해당 홈페이지를 웹스크래핑 함
# res = requests.get("http://nadocoding.tistory.com")
print("응답코드 :", res.status_code) # 200이면 정상

if res.status_code == requests.codes.ok: # status_code 값과 requests.codes.ok(=200) 값이 같으면
    print("정상입니다")
else:
    print("문제가 생겼습니다. [에러코드 ", requests.status_codes, "]")

res.raise_for_status() # 위 코드랑 같은 함수 사용
print("웹 스크리핑을 진행합니다")

print(len(res.text))
print(res.text) # res의 텍스트 값을 받아옴

with open("mygoogle.html", "w", encoding="utf8") as f: # 받아온 값을 파일로 저장
    f.write(res.text)