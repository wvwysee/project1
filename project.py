from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types

bot = telebot.TeleBot('6684976343:AAHQYaT3spQfdLZ9WKTqgB4a3d9mDHl-Z6Q')


@bot.message_handler(commands=['start'])
def start_com(message):
    bot.send_message(message.chat.id, f"wassup bre its NEWSbro_bot, write some commands to get some sauce, u feel me? {message.from_user.first_name}")

    @bot.message_handler(commands=['help'])
    def help_com(message):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Допомога'))
        bot.send_message(message.chat.id, '/start' '\n' '/getinfo' '\n' '/help' '\n' '/getsauce')

        @bot.message_handler(commands=['getinfo'])
        def getinfo_com(message):
            bot.send_message(message.chat.id, 'a keyword is entered from the keyboard and the bot finds the 10 latest news on the Internet and responds with headlines and links')

        @bot.message_handler(commands=['getsauce'])
        def gets_com(keyword):
         print("gotcha")
    url = 'https://www.nbcnews.com/world' 
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        news_articles = soup.find_all('article')  
        
        relevant_news = []
        for article in news_articles:
            headline = article.find('h2').get_text()  
            if keyword.lower() in headline.lower():  
                link = article.find('a')['href']  
                relevant_news.append((headline, link))
        
        if relevant_news:
            return relevant_news
        else:
            return [("По вашему запросу новостей не найдено.", "")]
    else:
        return [("Ошибка при получении страницы новостей.", "")]
      
     
    for headline, link in news_with_links:
        print(f"{headline}: {link}")

# Пример вызова функции:
keyword = input("Введите ключевое слово для поиска новостей: ")
gets_com(keyword)
bot.polling(none_stop=True)