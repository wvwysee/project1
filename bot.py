

import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler

def parse_news_with_links(keyword):
    url = 'https://www.nbcnews.com/world'  # замените 'https://example.com/news' на URL сайта, с которого вы хотите парсить новости
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        news_articles = soup.find_all('article')  # предполагается, что новости на сайте находятся в элементах <article>
        
        relevant_news = []
        for article in news_articles:
            headline = article.find('h2').get_text()  # предполагается, что заголовок новости находится в элементе <h2>
            if keyword.lower() in headline.lower():  # проверяем, содержит ли заголовок ключевое слово
                link = article.find('a')['href']  # предполагается, что ссылка на новость находится в элементе <a>
                relevant_news.append((headline, link))
        
        if relevant_news:
            return relevant_news
        else:
            return [("По вашему запросу новостей не найдено.", "")]
    else:
        return [("Ошибка при получении страницы новостей.", "")]

def start(update, context):
    update.message.reply_text("Привет! Я бот для поиска новостей. Введите /news <ключевое слово>, чтобы получить новости по этому слову.")

def news(update, context):
    keyword = " ".join(context.args)
    news_with_links = parse_news_with_links(keyword)
    for headline, link in news_with_links:
        update.message.reply_text(f"{headline}: {link}")

# Установка токена вашего бота
updater = Updater("6684976343:AAHQYaT3spQfdLZ9WKTqgB4a3d9mDHl-Z6Q", use_context=True)

# Добавление обработчиков команд
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('news', news))

# Запуск бота
updater.start_polling()
updater.idle()

















