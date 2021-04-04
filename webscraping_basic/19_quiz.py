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

elems = soup.find_all("table", attrs={"class":"tbl"})

for elem in elems:
    type = elem.find("td", attrs={"class":"col1"}).get_text()
    area = elem.find("td", attrs={"class":"col2"}).get_text()
    price = elem.find("td", attrs={"class":"col3"}).get_text()
    building = elem.find("td", attrs={"class":"col4"}).get_text()
    floor = elem.find("td", attrs={"class":"col5"}).get_text()
    for sale in range(1, 6):
        print("="*10, "매물 {}".format(sale), "="*10)
        print("거래 : ", type)
        print("면적 : ", area, "(공급/전용)")
        print("가격 : ", price, "(만원)")
        print("동 : ", building,)
        print("층 : ", floor)

browser.quit()