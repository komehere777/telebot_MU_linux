import requests
from bs4 import BeautifulSoup

req = requests.get('https://m.onoffmix.com/event/main?s=%EB%B0%8B%EC%97%85')
html = req.text
soup = BeautifulSoup(html, 'html5lib')
all_titles = soup.find_all('h1', {"class": "event_title"})
for title in all_titles:
    print(title.get_text())