## Магазин чаю

## Стек технологій

- Python
- SQLite
- Django
- Redis
- Celery
- RabbitMQ


Для роботи нашого магазину вам знадобляться наступні інструменти:


1. Створення та активація віртуального середовища:
   ```bash
   python3.9 -m venv ../venv
   source ../venv/bin/activate
   ```   
3. Встановлення залежностей
        pip install --upgrade pip
    pip install -r requirements.txt
    
   
## Запуск сервера RabbitMQ

3. Запуск сервера RabbitMQ:
    Встановлення (скачування) Docker-контейнера з RabbitMQ:
    ```bash 
   docker pull rabbitmq
    ```
4. Запуск сервера RabbitMQ та веб-інтерфейсу управління:
      ```bash
    docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
      ```
    
    RabbitMQ буде доступний за посиланням http://127.0.0.1:15672/
## Запуск Celery для обробки завдань:

5. Запуск Celery worker:
   ```bash
   celery -A myshop worker -l info
    ```
   
7. Запуск Celery Flower для відстеження стану задач:
   (Можна використовувати тільки RabbitMQ)
   ```bash
   celery -A myshop flower
   ```   
   Flower буде доступний за посиланням http://localhost:5555/dashboard.

## Запуск Redis для кешування:
7. Запуск Docker контейнера Redis:
   ```bash
   docker run -it --rm --name redis -p 6379:6379 redis
   ```     

## Команди для Stripe:

8. Використання Stripe CLI для прослуховування подій Stripe та перенаправлення їх на локальний сервер:
   ```bash
   Stripe login
   ```
   
   ```bash
            stripe listen --forward-to localhost:8000/payment/webhook/
   ```
