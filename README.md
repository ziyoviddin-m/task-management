 API-эндпоинты:

- http://127.0.0.1:8000/api/v1/task/ - для создание новой задачи и получение списка всех задач

- http://127.0.0.1:8000/api/v1/task/1/ - для получение задачи по идентификатору, обновление и удаление задачи

Дополнительные бонусные задачи:

1) Добавьте возможность прикрепления файлов к задачам - сделано
   
2)Реализуйте сортировку и фильтрацию задач по различным атрибутам:

- 127.0.0.1:8000/api/v1/task/?category=1 - фильтрация по категориям

- http://127.0.0.1:8000/api/v1/task/?ordering=creation_date - сортировка по дате создания задачи

- http://127.0.0.1:8000/api/v1/task/?search=Qwetrty - поиск по названии и описании задачи

3) Добавьте возможность добавления к задачам категорий или меток - сделано

Установка:
1) git clone https://github.com/ziyoviddin-m/task-management.git

2) python -m venv venv

3) .\venv\Scripts\activate

4) cd task-management

5) pip install -r requirements.txt

6) cd To_Do_List

7) python manage.py runserver

9) Админ панель

логин: admin

пароль: 1234
