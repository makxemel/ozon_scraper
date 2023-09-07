from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from parser.management.commands.tgbot import send_finish_message
from parser.serializers import ProductSerializer
from parser.models import Product

from bs4 import BeautifulSoup
import time
import math

from dotenv import load_dotenv
import os

load_dotenv()


def scraper(products_count):
    pages = math.ceil(products_count / int(os.getenv('PRODUCTS_PER_PAGE')))
    products = []

    for page in range(1, pages + 1):
        options = webdriver.ChromeOptions()
        options.add_argument("-headless=new")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get(os.getenv('URL_OZON_SHOP_TO_SCRAP') + f'?page={page}')
        time.sleep(10)

        html = driver.page_source
        driver.close()

        soup = BeautifulSoup(html, 'lxml')
        items_div = soup.find('div', class_='widget-search-result-container').find('div', recursive=False).findAll('div', recursive=False)
        for item in items_div:
            link = item.find('a', class_='tile-hover-target').get('href')
            title = item.find('span', class_='tsBody500Medium').text
            products.append({'title': title, 'link': 'https://www.ozon.ru' + link})

    # return only number of products what requested
    return products[:products_count]


def scrap_and_save_data(products_count=10):
    Product.objects.all().delete()
    scraped_data = scraper(products_count)
    if scraped_data:
        serializer = ProductSerializer(data=scraped_data, many=True)
        if serializer.is_valid():
            serializer.save()
            send_finish_message(products_count)
        return serializer