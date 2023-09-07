from src.celery import app
from parser.services import scrap_and_save_data


@app.task
def start_scrap(products_count=10):
    print('start scraping...')
    scrap_and_save_data(products_count)