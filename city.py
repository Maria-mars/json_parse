import json

import requests
from bs4 import BeautifulSoup

url = "https://www.mebelshara.ru/contacts"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
city_item = soup.find('div', {'class': 'city-item'})

final_list = []
while city_item is not None:
    city_name = city_item.find('h4', {'class': 'js-city-name'})
    shop_list_item = city_item.find('div', {'class': 'shop-list-item'})
    while shop_list_item is not None:
        shop_name = shop_list_item.get('data-shop-name')
        shop_address = shop_list_item.get('data-shop-address')
        data_shop_phone = shop_list_item.get('data-shop-phone')
        working_mode1 = shop_list_item.get('data-shop-mode1')
        working_mode2 = shop_list_item.get('data-shop-mode2')
        latitude = shop_list_item.get('data-shop-latitude')
        longitude = shop_list_item.get('data-shop-latitude')
        address = city_name.text + ", " + shop_address
        shop = {
            "address": address,
            "latlon": [latitude, longitude],
            "name": shop_name,
            "phones": [data_shop_phone],
            "working_hours": [working_mode1, working_mode2]
        }
        final_list.append(shop)
        shop_list_item = shop_list_item.next_sibling
    city_item = city_item.next_sibling
jsonList = json.dumps(final_list, ensure_ascii=False)
print(jsonList)

