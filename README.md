# Storage
RESTful API сервис для хранения товаров.

1.  CRUD API для всех моделей;
2. В админ-панели выведена в удобном виде информацию о записях в таблицах с возможностью поиска товаров;
3. Возможность увеличения количества товара по его штрихкоду;
4. Возможность уменьшения товара по ссылке;
5. UI документация ReDoc.

## Разверните репозиторий на своем серевере.

1. Клонируйте репозиторий:
```
git clone git@github.com:pitbul892/Storage.git
```
2. Создайте и активируйте виртуальное окружения:
```
py -m venv venv
source venv/bin/activate
```
3. Установите зависимости:
```
pip install -r requirements.txt
```
4. Примените миграции:
```
py manage.py migrate
py manage.py runserver
```
5. Создайте суперпользователя:
```
py manage.py createsuperuser
```
6. Запустите сервер разработки:
```
py manage.py runserver
```
Приложение будет доступно по адресу: ```http://127.0.0.1:8000/```
На странице ```http://127.0.0.1:8000/redoc/``` можно ознаомиться с документацией.
# API Эндпоинты
## Продукты
GET    /api/products/                  — Получить список всех продуктов

POST   /api/products/                  — Создать новый продукт

GET    /api/products/{id}/             — Получить продукт по ID

PUT    /api/products/{id}/             — Обновить продукт по ID

PATCH  /api/products/{id}/             — Частичное обновление продукта по ID

DELETE /api/products/{id}/             — Удалить продукт по ID

POST   /api/products/add_by_barcode/   — Добавить товар по штрихкоду

GET    /api/products/{id}/subtract/    — Уменьшить количество товара по ID


## Типы
GET    /api/types/                     — Получить список всех типов

POST   /api/types/                     — Создать новый тип

GET    /api/types/{id}/                — Получить тип по ID

PUT    /api/types/{id}/                — Обновить тип по ID

PATCH  /api/types/{id}/                — Частичное обновление типа по ID

DELETE /api/types/{id}/                — Удалить тип по ID
