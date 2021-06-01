from bs4 import BeautifulSoup
import requests
from random import *
from time import sleep
import csv

file = open('car.csv', 'w', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['სახელი', 'წელი', 'ძრავა', 'გარბენი', 'ტიპი', 'საჭე', 'ფასი'])

var = 1

url = 'https://www.myauto.ge/ka/s/00/0/00/00/00/00/00/6/avtomobilebi-kabrioleti?stype=0&currency_id=3&det_search=0&ord=7&category_id=6&keyword=&page=' + str(var)

while var < 6:

    r = requests.get(url)
    # print(r.url)
    # print(r.headers)
    content = r.text
    # print(content)
    soup = BeautifulSoup(content, 'html.parser')
    # print(soup)
    # print(r.status_code)

    block = soup.find('div', class_='search-lists-container')
    # print(block)
    all_car = block.find_all('div', class_='current-item')

    for each in all_car:
        name = each.h4.a.text
        name = name.replace('იყიდება ', '')
        engine = each.find('div', class_='car-detail-in cr-engine').p.text
        run = each.find('div', class_='car-detail-in cr-road').p.text
        typ = each.find('div', class_='car-detail-in cr-wheel').p.text
        wheel = each.find('div', class_='car-detail-in cr-ls cr-gas').p.text
        price = each.find('span', class_='car-price').text
        year = each.find('div', class_='car-name-right').p.text
        year = year.replace(' წ', '')
        # print(name)
        # print(engine)
        file_obj.writerow([name, year, engine, run, typ, wheel, price])
    var += 1
    sleep(randint(15, 20))




