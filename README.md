**Parser ozon products**

<hr/>

## Download

```bash
git clone https://github.com/makxemel/ozon_scraper.git
cd ozon_scraper
```

## Installation

<hr/>

### Presetting
1) Create an .env file and fill it with the pattern from example.env
env file:
> URL_OZON_SHOP_TO_SCRAP='https://www.ozon.ru/seller/1/products/'<br>
> PRODUCTS_PER_PAGE=36<br>
> PRODUCTS_COUNT=10<br>

> TOKEN = ''<br>
> BOT_USERNAME = ''<br>

> CELERY_BROKER_URL = "redis://localhost:6379"<br>
> CELERY_RESULT_BACKEND = "redis://localhost:6379"<br>

> DB_ENGINE='django.db.backends.postgresql'<br>
> DB_NAME='postgres'<br>
> DB_USER='postgres'<br>
> POSTGRES_PASSWORD='postgres'<br>
> DB_HOST='localhost'<br>
> DB_PORT=5432<br>

2) Install requirements
    ```bash
    pip install -r requirements.txt
    ```
3) Run docker-compose for installation Redis and database
   ```bash
   docker-compose up -d
   ```

   <hr/>

### Django

1) Migrations
   ```bash
   python manage.py migrate
   ```
2) Autocreate superuser (optional). **Login:** admin, **password**: admin
   ```bash
   python manage.py create_superuser
   ```
3) Run app
   ```bash 
   python manage.py runserver 
   ```
4) Start celery worker

   **Linux:**
   ```bash
   celery -A src.celery worker -B
   ```
   
   <hr/>

## Telegram

8)```bash
   python manage.py tgbot
   ```
   
<hr/>


## Documentation

### Admin panel

<a href="http://127.0.0.1:8000/admin/">Admin panel</a>

**Login:** admin

**Password:** admin

(p.s this username and password will be used by default if you followed step 2 from the django installation)

### Parsing
1) **GET/POST:** http://127.0.0.1:8000/v1/products/ get all products/start parsing
2) **GET:** http://127.0.0.1:8000/v1/products/<int:id> get a certain product

<hr/>

## Contacts

**Telegram:** https://t.me/makxemel