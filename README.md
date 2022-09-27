# Сервис уведомлений
Тестовое задание для кандидатов-разработчиков

## Задача
Необходимо разработать сервис управления рассылками API администрирования и получения статистики.

## Настроить проект
Нам нужно настроить приложение для правильной работы.

### Установить переменные среды
Чтобы безопасно взаимодействовать с проектом, нам нужно добавить несколько переменных среды в файл .env.

- `DB_NAME`
- `DB_USERNAME`
- `DB_PASSWORD`
- `BASE_URL`
- `TOKEN`

Нужные ключи вы можете найти у автора проекта.

## Запуск проекта
Для запуска проекта вам необходимо установить `docker`, после чего написать команду в командной строке в папке проекта

```bash
docker build .
docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose up --build
```

Откройте [http://localhost:8000](http://localhost:8000), чтобы просмотреть проект его в браузере.

Команда `docker-compose up --build` запускает проект с миграцией. Все необходимые зависимости проекта прописаны в файле [requirements.txt](https://github.com/Assylzhan-Izbassar/notification-service-app-api/blob/main/requirements.txt).

## Документация по API
Полную документацию проекта можно посмотреть запустив проект и перейти по [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/). URL откроет документацию в Swagger UI. </br>

### Основные конечные точки проекта
Основные endpoints по проекту с методами `GET`, `POST`, `PUT`, `PATCH` и `DELETE` </br>

- `http://127.0.0.1:8000/api/docs/#/` - документация проекта

#### Конечные точки для клиента
- `http://127.0.0.1:8000/notification/clients/` - для просмотра списка клиентов и создание нового клиента </br>
- `http://127.0.0.1:8000/notification/clients/{id}/` - для просмотра детали клиента, обновление его данных или удаление

#### Конечные точки для рассылки
- `http://127.0.0.1:8000/notification/distributions/` - для просмотра списка рассылок и создание новой рассылки </br>
- `http://127.0.0.1:8000/notification/distributions/{id}/` - для просмотра детали рассылки, обновление его данных или удаление

#### Конечные точки для сообщение
- `http://127.0.0.1:8000/notification/messages/` - для просмотра списка сообщений и создание нового сообщения

- `http://127.0.0.1:8000/notification/messages/{id}/` - для просмотра детали сообщения, обновление его данных или удаление

#### Дополнительные конечные точки
- `http://127.0.0.1:8000/admin/` - страница админа

- `http://127.0.0.1:3000/` - страница smtp4dev

## Описание реализованных методов
Для выполнение логики рассылки в пути `notification/tasks.py` создал метод `send_distribution`, который отвечает на отправку рассылки. Для того чтобы рассылка было отправление после создание нового объекта, использовал `signals` в `django`, в частности `post_save` методом `distribution_post_save`, который находиться в пути `notification/signals.py`.

</br>
</br>

<ins>Из методов дополнительных задач,</ins> для того чтобы **отправить статистику по обработанным рассылкам на email** создал метод `send_report` в пути `notification/tasks.py`, который в 12:00 каждый день автоматически отправляет сообщение с помощью `celery-beat` на email через сервер для разработки `smtp4dev`.

## Выполненные дополнительные задания

- Подготовить docker-compose для запуска всех сервисов проекта одной командой
- Сделать так, чтобы по адресу /docs/ открывалась страница со Swagger UI и в нём отображалось описание разработанного API. Пример: https://petstore.swagger.io
- Реализовать администраторский Web UI для управления рассылками и получения статистики по отправленным сообщениям
- Реализовать дополнительный сервис, который раз в сутки отправляет статистику по обработанным рассылкам на email
