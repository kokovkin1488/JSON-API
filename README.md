# JSON-API
Test for Nortex
JSON API блога с высокой оптимизацией БД

test file - https://docs.google.com/document/d/1iy83ZGBd7FZiE88jUCKxUm1MfsLxM56EJzg54iW3c8E/edit#heading=h.o3neejcunayy

##Доступ к административной части
    login: admin
    password: P@ssw0rd
    
##Доступ к базе данных
    name: json_api_db
    user: json_api_user
    password: P@ssw0rd
    
##Старт сервера
    python manage.py runserver
    
Установка зависимостей (Django)
 
    pip install -r requirements.txt
    
Обновление файла зависимостей (Django)

    pip freeze > requirements.txt
    
Накатить миграцию

    python manage.py migrate