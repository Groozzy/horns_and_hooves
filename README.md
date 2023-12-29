# Рога и копыта
Репозиторий является решением для тестового задания по созданию API для магазина «Рога и Копыта».

### Внимание!
Перед запуском проекта в коренной директории необходимо создать файл .env и заполнить по следующему шаблону:

~~~
DEBUG=False
SECRET_KEY=<Секретный ключ из settings.py>
ALLOWED_HOSTS=<Хост>
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<Пароль>
DB_HOST=db
DB_PORT=5432
~~~

##### В проекте реализованы мультиконтейнерные приложения (Docker compose).

Для запуска проекта из коренной директории необходимо выполнить команду:

~~~
docker compose up
~~~

В последствии выполнится запуск мультиконтейнерного приложения.

##### Далее необходимо подтянуть статику django:

Выполните последовательно следующие команды:

~~~
docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /app/collected_static/. /backend_static/static/ 
~~~

Проект доступен по адресу https://127.0.0.1:80/

##### С функционалом проекта можно ознакомиться в документации Redoc
По адресу https://127.0.0.1:80/redoc/