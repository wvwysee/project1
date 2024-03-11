import requests
import json
import telebot
import time

bot = telebot.TeleBot('6684976343:AAHQYaT3spQfdLZ9WKTqgB4a3d9mDHl-Z6Q')

@bot.message_handler(commands=['start'])
def start(message):
    if len(message.text.split()) == 1:
        bot.reply_to(message, "Please enter a keyword to search for news.")
        time.sleep(10)

    keyword = input("fsfs:  ")
    api_key = 'L64425K9qx3YSBP9gho7fpSj1ur3ENSI'
    news_data = get_news(keyword, api_key)

    if news_data:
        for i in range(min(10, len(news_data['titles']))):
            headline = news_data['titles'][i]
            link = news_data['links'][i]
            bot.reply_to(message, f"{headline}: {link}")
    
       
        filename = f"{keyword}_news.json"
        with open(filename, 'w') as f:
            json.dump(news_data, f, indent="2")

        
        with open(filename, 'rb') as f:
            bot.send_document(message.chat.id, f)

    else:
        bot.reply_to(message, "No news found for the given keyword.")

def get_news(keyword, api_key):
    api_url = f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q={keyword}&api-key={api_key}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            articles = data['response']['docs']
            
            titles = []
            links = []
            times = []
            for article in articles:
                titles.append(article['headline']['main'])
                links.append(article['web_url'])
                times.append(article['pub_date'])
           
            news_data = {
                'titles': titles,
                'links': links,
                'times': times
            }
            return news_data
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None

bot.polling(none_stop=True) 