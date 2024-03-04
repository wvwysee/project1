import keyword
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types

bot = telebot.TeleBot('6684976343:AAHQYaT3spQfdLZ9WKTqgB4a3d9mDHl-Z6Q')

parsed_news = []

def parser(keywordd):
    global parsed_news
    print("gotcha")
    url = 'https://www.nbcnews.com/world' 
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        news_articles = soup.find_all('article')  
        
        relevant_news = []
        for article in news_articles:
            headline = article.find('h2').get_text()  
            if keywordd.lower() in headline.lower():  
                link = article.find('a')['href']  
                relevant_news.append((headline, link))
        
        parsed_news = relevant_news

@bot.message_handler(commands=['start'])
def start(message):
    global parsed_news
    if len(message.text.split()) == 1:
        bot.reply_to(message, "Please enter a keyword to search for news.")
        
    
    keywordd = ' '.join(message.text.split()[1:])
    parser(keywordd)
    
    if parsed_news:
        for headline, link in parsed_news:
            bot.reply_to(message, f"{headline}: {link}")

bot.polling(none_stop=True)