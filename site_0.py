import requests
from bs4 import BeautifulSoup
from time import sleep


headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

def downloadimages(url):                    # ЗАГРУЗКА КАРТИНОК!
    resp = requests.get(url, stream=True)   # картинки будут загружаться порционно
    with open("E:\\python\\parser\\images\\" + url.split('/')[-1],  "wb") as file2:     # url.split('/')[-1] - имя файла, часть ссылки
        for value in resp.iter_content(1024*1024):   # колличество байт за 1 проход. 1Мб оптимально
            file2.write(value)


def list_card():
    for count in range(1, 3):       # до 8, на сайте 7 страниц
        sleep(1)
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')     # lxml парсер html
        # if soup:                # True если диапазон 200-300    response.status_code
        #     print(soup)
        data = soup.findAll('div', class_="col-lg-4 col-md-6 mb-4")    # карточка товара

        for i in data:
            # name = i.find('h4', class_="card-title").text.replace('\n', '')     #  название
            # price = i.find('h5').text        # цена
            # img = r'https://scrapingclub.com/exercise/list_basic/?page=1' + i.find('img', class_="card-img-top img-fluid").get('src')    # картинка
            # print(name + '\n' + price + '\n' + img + '\n')
            card_url = 'https://scrapingclub.com' + i.find('a').get('href')
            yield card_url

def url_cards():
    for url_c in list_card():
        sleep(3)
        response = requests.get(url_c, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('div', class_="card mt-4 my-4")
        name = data.find('h3', class_="card-title").text
        price = data.find('h4').text
        img = 'https://scrapingclub.com/' + data.find('img', class_="card-img-top img-fluid").get('src')
        description = data.find('p', class_="card-text").text
        #print(name + '\n' + price + '\n' + img + '\n' + description + '\n')
        downloadimages(img)
        yield name, price, img, description