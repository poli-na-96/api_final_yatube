# api_final

Проект yatube это социальная сеть, где пользователь может публиковать посты, подписываться на других пользователей, оставлять комментарии под другими постами. 
В данном проекте представлен backend api yatube, то есть это внутренняя часть продукта, которая находится на сервере и скрыта от пользователей. 

**Как запустить проект:**
Клонировать репозиторий и перейти в него в командной строке:

git clone git@github.com:poli-na-96/api_final_yatube.git
cd api_final_yatube
Cоздать и активировать виртуальное окружение:

python3 -m venv venv
source venv/Scripts/activate
Установить зависимости из файла requirements.txt:

pip install -r requirements.txt
Выполнить миграции:

python manage.py migrate
Запустить проект:

python manage.py runserver

**Примеры запросов:**
POST запрос на http://127.0.0.1:8000/api/v1/jwt/create/:
"""Получаем JWT-токен"""
{
"username": "string",
"password": "string"
}
Ответ на запрос:
{
"refresh": "string",
"access": "string"
}

GET запрос на http://127.0.0.1:8000/api/v1/posts/: 
    """Получаем список постов"""
Ответ на запрос:
{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
{}
]
}

POST запрос на http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/:
    """Создаем комментарий"""
{
"text": "string"
}
Ответ на запрос:
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}

POST запрос на http://127.0.0.1:8000/api/v1/follow/:
    """Оформляем подписку на пользователя"""
{
"following": "string"
}
Ответ на запрос:
Copy
{
"user": "string",
"following": "string"
}

**Стек технологий:** python, django, SQlite, rest api, jwt, git
