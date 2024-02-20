

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
        def main(message):
            

bot.polling(none_stop=True)

















