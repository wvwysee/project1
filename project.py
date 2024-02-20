from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types

bot = telebot.TeleBot('6684976343:AAHQYaT3spQfdLZ9WKTqgB4a3d9mDHl-Z6Q')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'wassup bre its NEWSbro_bot, write some commands to get some sauce, u feel me? {message.from_user.first_name}')

    @bot.message_handler(commands=['help'])
    def main(message):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Допомога'))
        bot.send_message(message.chat.id, '/start' '\n' '/getinfo' '\n' '/help' '\n' '/getsauce')

        @bot.message_handler(commands=['getinfo'])
        def main(message):
            bot.send_message(message.chat.id, 'a keyword is entered from the keyboard and the bot finds the 10 latest news on the Internet and responds with headlines and links')



        @bot.message_handler(commands=['getsauce'])
        def main (message,update: Update, context: CallbackContext):
            

    word_to_search = context.args[0]

    
    url = "https://www.nbcnews.com/world"

    
    response = requests.get(url)
    
    
    if response.status_code == 200:
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        
        links = soup.find_all('a', href=True)
        
        
        articles_found = 0
        
      
        for link in links:
            article_url = link['href']
            
            if link.text.strip() and article_url != url:
                article_response = requests.get(article_url)
                if article_response.status_code == 200:
                    article_soup = BeautifulSoup(article_response.text, 'html.parser')
                  
                    if word_to_search in article_soup.get_text():
                        update.message.reply_text(f"Статья: {link.text.strip()}\nСсылка: {article_url}")
                        articles_found += 1
                      
                        if articles_found >= 10:
                            break
    else:
        
        update.message.reply_text("Ошибка при выполнении запроса")

def main():
    
    updater = Updater("6684976343:AAHQYaT3spQfdLZ9WKTqgB4a3d9mDHl-Z6Q")
    dispatcher = updater.dispatcher
    
    
    dispatcher.add_handler(CommandHandler("search", search_articles))

    
    updater.start_polling()
    updater.idle()


bot.polling(none_stop=True)


