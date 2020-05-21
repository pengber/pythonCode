import csv
import requests
from bs4 import BeautifulSoup
def getAarts():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'Host': 'beijing.anjuke.com'
    }
    link = 'https://beijing.anjuke.com/sale/'
    r = requests.get(link, headers= headers)

    soup = BeautifulSoup(r.text, 'lxml')
    house_list = soup.find_all('li', class_="list-item")

    csvFile = open('apartments.csv', 'a+', newline='',encoding='utf-8')
    w = csv.writer(csvFile)

    for house in house_list:
        house_info = []
        title = house.find('a', class_ = 'houseListTitle').get_text()
        rooms = house.find('div', class_ = 'details-item').contents[1].get_text()
        area = house.find('div', class_ = 'details-item').contents[3].get_text()
        floor = house.find('div', class_ = 'details-item').contents[5].get_text()
        year = house.find('div', class_ = 'details-item').contents[7].get_text()
        where = house.find('span', class_ = 'comm-address').get_text()
        price = house.find('span', class_= 'price-det').get_text()
        price_per = house.find('span', class_ = 'unit-price').get_text()
        house_info.append(title)
        house_info.append(rooms)
        house_info.append(area)
        house_info.append(floor)
        house_info.append(year)
        house_info.append(where)
        house_info.append(price)
        house_info.append(price_per)
        print (house_info)
        w.writerow(house_info)
    
    csvFile.close()
getAarts()