import telebot
from telebot import types

bot = telebot.TeleBot('6548496739:AAGrzcsKDKzqV-1uLRMUVvuLwLieoa5auv0')

@bot.message_handler(commands=['start'])

def start(message):

    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('whatbotcando')
    markup.row(btn1)
    btn2 = types.KeyboardButton('whatbotcando')
    markup.row(btn2)
    btn3 = types.KeyboardButton('getnews ')
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Привіт', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)



    def on_click(message):
        if message.text == 'whatbotcando':
            bot.send_message(message.chat.id, 'You can click ob button "getnews" and enter 1 keyword, then "NewsBOT" will respond with 10 lastest news and links to them!')
        elif message.text == 'abotcreator':
            bot.send_message(message.chat.id, 'Person that created me is known as "Bilousov Oleksandr')
        elif message.text == 'getnews':
            bot.send_message(message.chat.id, 'Enter 1 keyword')
            input(message)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,f'Привіт,{message.from_user.first_name}')

    @bot.message_handler(commands=['help'])
    def main(message):
        bot.send_message(message.chat.id,'/start''\n' '/menu' '\n' '/help')

        @bot.message_handler(commands=['menu'])
        def main(message):
            bot.send_message(message.chat.id, 'Головне меню')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привіт':
        bot.send_message(message.chat.id,f'Привіт,{message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message,f'ID:{message.from_user.id}')

bot.polling(none_stop=True)