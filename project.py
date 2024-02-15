import requests
from bs4 import BeautifulSoup

# Функция для выполнения парсинга по заданному слову и вывода ссылок на статьи
def parse_website(url, target_word, max_articles=10):
    # Выполняем GET-запрос к веб-странице
    response = requests.get(url)
    
    # Проверяем успешность запроса
    if response.status_code == 200:
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Ищем все ссылки на странице
        links = soup.find_all('a', href=True)
        
        # Счетчик найденных статей
        articles_found = 0
        
        # Проходим по каждой ссылке и проверяем наличие заданного слова
        for link in links:
            article_url = link['href']
            # Игнорируем ссылки без текста и ссылки на ту же страницу
            if link.text.strip() and article_url != url:
                article_response = requests.get(article_url)
                if article_response.status_code == 200:
                    article_soup = BeautifulSoup(article_response.text, 'html.parser')
                    # Поиск заданного слова в тексте статьи
                    if target_word in article_soup.get_text():
                        print(f"Статья: {link.text.strip()}")
                        print(f"Ссылка: {article_url}")
                        print()
                        articles_found += 1
                        # Выходим из цикла, если достигнуто максимальное количество статей
                        if articles_found >= max_articles:
                            break
    else:
        # В случае ошибки выводим сообщение
        print("Ошибка при выполнении запроса:", response.status_code)

# Пример использования функции
url = "hhttps://www.nbcnews.com/world"
word_to_search = "fight"
parse_website(url, word_to_search)