from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import Car

import requests
from bs4 import BeautifulSoup

def index(request):

    for p in range(1, 5):
        print(p)

        url = f'https://auto.ria.com/uk/car/used/?page={p}'

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')

        cars = soup.findAll('section', class_='ticket-item')

        cars_list = []

        for car in cars:
            cars_obj = Car.objects.all()
            car_link = car.find('a', class_='address').get('href')
            car_card = requests.get(car_link)
            car_soup = BeautifulSoup(car_card.text, 'lxml')

            car_number = car_soup.find('main', class_='auto-content').find('div', class_='t-check').findAll('span')
            car_vin = car_soup.find('main', class_='auto-content').find('div', class_='t-check').findAll('span')

            if len(car_number) > 1:
                car_number = car_number[0].text
            else:
                car_number = None

            if len(car_vin) > 1:
                car_vin = car_vin[-1].text
            else:
                car_vin = car_vin[0].text



            car_data = {
                'url': car_link,
                'title': car_soup.find('div', class_='ticket-status-0').find('h1', class_='head').get('title'),
                'price_usd': int(''.join(car_soup.find('div', class_='ticket-status-0').find('div', class_='price_value').find('strong', class_="").text.split()[0:2])),
                'odometer': int(car_soup.find('div', class_='ticket-status-0').find('div', class_='base-information').find('span').text + '000'),
                'username': car_soup.find('div', class_='ticket-status-0').find('span', class_='seller_info_img').find('img', class_='img').get('title'),
                'phone_number': car_soup.find('div', class_='phones_list').find('span', class_="mhide").text,
                'image_url': car_soup.find('div', class_='carousel-inner').find('source').get('srcset'),
                'images_count': int(car_soup.find('main', class_='auto-content').find('a', class_='show-all').text.split()[2]),
                'car_number': car_number,
                'car_vin': car_vin,
            }

            car_char = list(car_data.items())
            cars_list.append(car_char)

            

        for car_info in cars_list:
            to_db = Car(url = car_info[0][1], title = car_info[1][1], price_usd = car_info[2][1], otometer = car_info[3][1], username = car_info[4][1], phone_number = car_info[5][1],
                    image_url = car_info[6][1], images_count = car_info[7][1], car_number = car_info[8][1], car_vin = car_info[9][1])
            

            current_url = car_info[0][1]

            if Car.objects.filter(url=current_url).exists():
                continue
            else:
                to_db.save()

        print(cars_obj)  
        data = {
            'cars': cars_obj
        }

    return render(request, 'oldcars/index.html', data)



def page_not_found(request, exeption):
    return HttpResponseNotFound("<h1>Page not found</h1>")
