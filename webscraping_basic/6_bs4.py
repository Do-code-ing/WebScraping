import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# 가져온 res.text값을 lxml을 통해 beautifulsoup객체로 만듬
# print(soup.title) # soup객체의 element에 바로 접근 가능
# print(soup.title.get_text()) # text정보만
# print(soup.a) # soup 객체에서 처음 발견되는 a를 출력
# print(soup.a.attrs) # a element의 속성 정보를 출력
# print(soup.a["href"]) # a element의 href 속성 '값' 정보를 출력
# # 잘 알 때나 가능
# # 모를 땐 find 
# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # a tag아래의 attributes의 elements를 찾아줌
# print(soup.find(attrs={"class":"Nbtn_upload"})) # 찾으려는 객체가 하나라면 a tag can be excepted
# print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li") # .next_sibling.next_sibling 대체 가능
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="여신강림-144화")
print(webtoon)
