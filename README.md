# Homework16
Проект "Управление пользователями, заказами и предложениями"
Проект представляет собой простую веб-приложение на основе Flask, которое позволяет управлять пользователями, заказами и предложениями. В приложении используется база данных SQLite для хранения информации.

Установка и запуск
Установите необходимые зависимости, выполнив команду:

Copy code
pip install -r requirements.txt
Создайте базу данных и таблицы, выполнив файл database.py:

Copy code
python database.py
Запустите приложение, выполнив файл app.py:

Copy code
python app.py
После запуска приложение будет доступно по адресу http://localhost:5000.

API Endpoints
Пользователи
GET /users - Получить список всех пользователей.
GET /users/<user_id> - Получить информацию о пользователе по идентификатору.
POST /users - Создать нового пользователя.
PUT /users/<user_id> - Обновить информацию о пользователе.
DELETE /users/<user_id> - Удалить пользователя.
Заказы
GET /orders - Получить список всех заказов.
GET /orders/<order_id> - Получить информацию о заказе по идентификатору.
POST /orders - Создать новый заказ.
PUT /orders/<order_id> - Обновить информацию о заказе.
DELETE /orders/<order_id> - Удалить заказ.
Предложения
GET /offers - Получить список всех предложений.
GET /offers/<offer_id> - Получить информацию о предложении по идентификатору.
POST /offers - Создать новое предложение.
PUT /offers/<offer_id> - Обновить информацию о предложении.
DELETE /offers/<offer_id> - Удалить предложение.
Примеры запросов
Получить список всех пользователей:

bash
Copy code
GET /users
Получить информацию о пользователе с идентификатором 1:

bash
Copy code
GET /users/1
Создать нового пользователя:

bash
Copy code
POST /users
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "password": "password123"
}
Обновить информацию о пользователе с идентификатором 1:

bash
Copy code
PUT /users/1
Content-Type: application/json

{
  "name": "John Smith",
  "email": "john.smith@example.com",
  "password": "newpassword"
}
Удалить пользователя с идентификатором 1:

bash
Copy code
DELETE /users/1
Аналогичные запросы можно выполнять для заказов и предложений, заменив /users на /orders или /offers в соответствующих URL.
