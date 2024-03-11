import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


browser = webdriver.Chrome()


browser.get('https://www.bbc.co.uk/search?q=')
keyword = input("ENTER WORD:  ")

search_box = browser.find_element("name",'q')
search_box.send_keys(keyword)
search_box.send_keys(Keys.RETURN)


soup = BeautifulSoup(browser.page_source, 'html.parser')
news_results = soup.find_all('div', class_='BVG0Nb')


news_list = []


for result in news_results:
    link = result.a['href']
    title = result.text
    time = result.find('span', class_='WG9SHc').text
    news_item = {'title': title, 'link': link, 'time': time}
    news_list.append(news_item)


browser.quit()


with open('news.json', 'w') as f:
    json.dump(news_list, f)

print("Данные сохранены в файл news.json")





