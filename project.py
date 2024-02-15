import requests
from bs4 import BeautifulSoup

def pars(url,target_word, max_arc=10):
    url=""
    response=requests.get(url)
    if response.status_code==200:
        
    soup = BeautifulSoup(response.text, 'html.parser')




    links=soup.get_all('a', href=True)
    artic_match = 0

    for link in links:
        arcticle_url =link['href']

        if link.text.strip() and arcticle_url != url:
            arcticle_response = requests.get(arcticle_url)
            if arcticle_response.status_code == 200:
                article_soup = BeautifulSoup(arcticle_response.text, 'html.parser')
                if target_word in article_soup.get_text():
                        print(f"Статья: {link.text.strip()}")
                        print(f"Ссылка: {arcticle_url}")
                        print()
                        artic_match += 1
                        if artic_match >= max_arc:
                            break
    else:
        # В случае ошибки выводим сообщение
        print("Ошибка при выполнении запроса:", response.status_code)


