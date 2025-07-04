Данный проект - это CRM-система, написанная на Django
========
Данная система предоставляет такой функционал: 


Создание, просмотр, редактирование услуг 


Создание, просмотр, редактирование рекламных кампаний 


Создание, просмотр, редактирование потенциальных и активных клиентов 


Создание, просмотр, редактирование контрактов 


Просмотр статистики по проведенным рекламным кампаниям 

Установка
=======
1. ```git clone https://github.com/ninja152play/Dgano-site.git```
2. ```cd CRM```
3. ```docker build -t django-app .```

Запуск
======
```docker run -d -p 8000:8000 --restart unless-stopped django-app```

Документация
===========

## Роли пользователей


Администратор может создавать, просматривать и редактировать пользователей, назначать им роли и разрешения. Такой функционал реализует административная панель Django.


Оператор может создавать, просматривать и редактировать потенциальных клиентов.


Маркетолог может создавать, просматривать и редактировать предоставляемые услуги и рекламные кампании.


Менеджер может создавать, просматривать и редактировать контракты, смотреть потенциальных клиентов и переводить их в активных.


Все роли могут смотреть статистику рекламных кампаний.


### Авторизация и ацетификация построена на sessions и cookies

## Создание админа


1. ```docker ps -a # сопируем CONTAINER ID```

2. ```docker exec -it CONTAINER ID /bin/bash```

3. ```cd crm```

4. ```python manage.py createsuperuser```

5. ```exit```
Доступ в админ-панель по ссылке http://server_ip:8000/admin