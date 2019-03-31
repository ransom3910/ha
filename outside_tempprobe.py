#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests


def get_temp():
    try:
        page = requests.get("https://weather.com/weather/today/l/46113:4:US")
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            data = soup.find(class_="today_nowcard-temp")
            print(data.get_text().strip("°"))
        else:
            print("Offline")
    except Exception as err:
        print("Offline")
        exit(0)


if __name__ == '__main__':
    get_temp()
