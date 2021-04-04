from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True # headless 적용
options.add_argument("window-size=1920x1080") # 화면 값 정의
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\ Chrome/88.0.4324.182 Safari/537.36")
# user-agent 값 정의
browser = webdriver.Chrome(options=options) # 옵션 값 적용
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()