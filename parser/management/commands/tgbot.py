from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import TeleBot
from dotenv import load_dotenv
import os
from parser.models import Product

load_dotenv()


# Объявление переменной бота
bot = TeleBot(os.getenv('TOKEN'), threaded=False)

def send_finish_message(products_count):
    bot.send_message(284669246, 'Задача на парсинг товаров с сайта Ozon завершена.' + '\n' + f'Сохранено: {products_count} товаров.')


class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        @bot.message_handler(commands=['list_of_products'])
        def send_products(message):
            products = Product.objects.all()
            print(message.chat.id)
            for product in products:
                bot.reply_to(message, f'{product.title}\n{product.link}')
        bot.enable_save_next_step_handlers(delay=2) # Сохранение обработчиков
        bot.load_next_step_handlers()   # Загрузка обработчиков
        bot.infinity_polling()