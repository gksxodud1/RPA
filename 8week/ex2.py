from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


query = input('검색할 키워드를 입력하세요:')

url='https://www.naver.com/'

driver = webdriver.Chrome() #여기서부터 작동 자동화 코드
driver.get(url)
time.sleep(3)
#selenium -> 작동 자동화 데이터 사이트 접속- 접근
search_box = driver.find_element(By.CSS_SELECTOR,'#APjFqd')   #동작에 필요한 엘리먼트 조작
#1엘리먼트를 찾는다 2마우스,키 입력

search_box.send_keys("KBO 한국시리즈")
search_box.send_keys(Keys.RETURN)  
time.sleep(8)





driver.find_element(By.CSS_SELECTOR,'#lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_flicking_wrap._conveyer_root > div:nth-child(8) > a').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'#lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_flicking_wrap._conveyer_root > div:nth-child(2) > a').click()
time.sleep(3)


news_titles = driver.find_elements(By.CSS_SELECTOR,",news_tit")
print(news_titles)

for i in news_titles :
    title = i.text
    href = i.get_attribute('href') #링크속성       href
    print(title , " :", href)
    ##크롤링을 통해서 데이터 추출해서 분석 