import telebot
from telebot import types

bot = telebot.TeleBot('6548496739:AAGrzcsKDKzqV-1uLRMUVvuLwLieoa5auv0')
@bot.message_handler(commands=['start'])
def ques(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    

    whatbotcando = types.InlineKeyboardMarkup('whatbotcando', callback_data='You can click ob button "getnews" and enter 1 keyword, then "NewsBOT" will respond with 10 lastest news and links to them!')
    aboutcreator = types.InlineKeyboardMarkup('aboutcreator', callback_data='Person that created me is known as "Bilousov Oleksandr')
    getnews = types.InlineKeyboardMarkup('getnews', callback_data='Enter 1 keyword')

    markup.add(whatbotcando,aboutcreator,getnews)


    bot.send_message(message.chat.id, 'What u want to know?', reply_markup=markup)
#@bot.callback_query_handler(func=lambda call:True)
#def answ(callb):
    bot.polling()