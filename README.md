
# Интерфейс для сайта Hacker News

## Комментарии
Проект недоделан. Выполнена чать бэкенда. Общий скелет есть. 

## Технологии

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

## Запуск проекта в dev-режиме

- Клонируйте репозиторий с проектом на свой компьютер
```bash
git clone https://github.com/Luna-luns/Hacker_news_site.git
```

- Установите и активируйте виртуальное окружение

```bash
python3 -m venv venv
source venv/bin/activate
```

- Установите зависимости из файла requirements.txt

```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

### Выполните миграции и создайте суперпользователя:
```bash
python3 manage.py migrate
python3 manage.py createsuperuser
```

### Загрузите статику:
```bash
python3 manage.py collectstatic --no-input
```

### Логин и пароль администратора:
```bash
admin9
admin9admin
```

## Автор:  
_Струнникова Елизавета_<br>
**email**: _liza.strunnikova@yandex.ru_<br>
