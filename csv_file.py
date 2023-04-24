import csv
from site_0 import url_cards

columns = ['name', 'price', 'images', 'descriptions']
with open('base_cards', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    for row in url_cards():
        writer.writerow(row)


# Запуск файла отсюда!