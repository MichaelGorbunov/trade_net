 

Задание
В данном задании вам предлагается разработать онлайн платформу-торговой сети электроники. Общая информация

    Тестовое задание состоит из нескольких задач. Мы примем вашу кандидатуру к рассмотрению только в том случае, если работа выполнена целиком. Попытайтесь продемонстрировать ваш уровень опыта и навыков в каждой задаче, чтобы мы смогли в полной мере оценить вашу кандидатуру.
    Вы должны отправить ваше готовое приложение в виде ссылки на GitHub- или GitLab-репозиторий. Если вы пришлете приложение в любом другом виде (в виде ссылки на zip-архив, прикрепите zip-архив к письму и др.), ваша кандидатура не будет нами рассмотрена!
    Если вы сделали не все пункты тестового задания — пожалуйста, укажите причину, по которой вы их не выполнили (не хватило времени, не хватило опыта/знаний, что-то еще).

Технические требования

    Python 3.8+
    Django 3+
    DRF 3.10+
    PostgreSQL 10+

При выполнении тестового задания вы можете дополнительно использовать любые сторонние Python-библиотеки без всяких ограничений.
Задание

    Создайте веб-приложение с API-интерфейсом и админ-панелью.
    Создайте базу данных, используя миграции Django.

Требования к реализации:

    Необходимо реализовать модель сети по продаже электроники.

    Сеть должна представлять собой иерархическую структуру из трех уровней:
        завод;
        розничная сеть;
        индивидуальный предприниматель.

    Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, т. е. завод всегда находится на уровне 0, а если розничная сеть относится напрямую к заводу, минуя остальные звенья, ее уровень — 1.
    Каждое звено сети должно обладать следующими элементами:
        Название.
        Контакты:
            email,
            страна,
            город,
            улица,
            номер дома.
        Продукты:
            название,
            модель,
            дата выхода продукта на рынок.
        Поставщик (предыдущий по иерархии объект сети).
        Задолженность перед поставщиком в денежном выражении с точностью до копеек.
        Время создания (заполняется автоматически при создании).
    Сделать вывод в админ-панели созданных объектов.

    На странице объекта сети добавить:
        ссылку на «Поставщика»;
        фильтр по названию города;
        admin action, очищающий задолженность перед поставщиком у выбранных объектов.
    Используя DRF, создать набор представлений:

    CRUD для модели поставщика (запретить обновление через API поля «Задолженность перед поставщиком»).

    Добавить возможность фильтрации объектов по определенной стране.

## Инструкции по запуску

1. Клонировать проект
```
git clone --branch develop --single-branch https://github.com/MichaelGorbunov/trade_net
```
2. Установить необходимые зависимости с помощью 
`poetry install --no-root  `.
3. Создать файл .env на основе .env_sample
4. Средствами postgresql или через кастомную команду создать базу данных с именем, указанным в .env.
```
python manage.py create_db
```
5. Создать и выполнить миграции 
```
python manage.py makemigrations
python manage.py migrate
```
5. Создать суперпользователя (администратора) командой:

```
python manage.py csu
```
6. Запустить сервер разработки с помощью 
```
python manage.py runserver
```
7. Войти в админ-панель по адресу `http://localhost:8000/admin/` 
и начать управление объектами.

8. Перед началом работы нужно получить токен для пользователя.
9. Основные эндпоинты расположены по адресам:
```
http://127.0.0.1:8000/users/-работа с пользователями
http://127.0.0.1:8000/users/login/-авторизация
http://127.0.0.1:8000/api/nodes/-работа с юнитами торговой сети

```
10. Готовые данные для модели TradeNode можно загрузить
```commandline
python manage.py loaddata trade_node_fixture.json --format json
```
11. Минимальная коллекция для использования с Postman содержится в файле trade_network.postman_collection.json