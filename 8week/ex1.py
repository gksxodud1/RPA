from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
url='https://www.google.co.kr/'

driver = webdriver.Chrome() #여기서부터 작동 자동화 코드
driver.get(url)
time.sleep(3)
#selenium -> 작동 자동화 데이터 사이트 접속- 접근
search_box = driver.find_element(By.CSS_SELECTOR,'#APjFqd')   #동작에 필요한 엘리먼트 조작
#1엘리먼트를 찾는다 2마우스,키 입력

search_box.send_keys("KBO 한국시리즈")
search_box.send_keys(Keys.RETURN)  
time.sleep(20)