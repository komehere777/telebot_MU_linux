from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS('/usr/local/bin/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
driver.implicitly_wait(3)
driver.get('https://m.onoffmix.com/event/main?s=%EB%B0%8B%EC%97%85')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
all_divs = soup.find_all('h1', {"class": "event_title"})
for title in all_divs:
    print(title.get_text())