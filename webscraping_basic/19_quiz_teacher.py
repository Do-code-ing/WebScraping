import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.maximize_window()

url = "http://daum.net"
headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"

browser.get(url)
browser.find_element_by_xpath("//*[@id='q']").send_keys("송파 헬리오시티")
browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]").click()

time.sleep(2)

soup = BeautifulSoup(browser.page_source, "lxml")

elems = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")

for idx, elem in enumerate(elems):
    infor = elem.find_all("td")

    print("="*10, f"매물 {idx+1}", "="*10)
    print("거래 : ", infor[0].get_text().strip())
    print("면적 : ", infor[1].get_text().strip(), "(공급/전용)")
    print("가격 : ", infor[2].get_text().strip(), "(만원)")
    print("동 : ", infor[3].get_text().strip())
    print("층 : ", infor[4].get_text().strip())

browser.quit()