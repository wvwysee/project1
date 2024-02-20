from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup


def search_articles(update: Update, context: CallbackContext):

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
    
    updater = Updater("6548496739:AAGrzcsKDKzqV-1uLRMUVvuLwLieoa5auv0")
    dispatcher = updater.dispatcher
    
    
    dispatcher.add_handler(CommandHandler("search", search_articles))

    
    updater.start_polling()
    updater.idle()



if __name__ == '__main__': 
    main()