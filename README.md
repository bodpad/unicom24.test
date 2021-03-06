## Развертывание и запуск
```
git clone https://github.com/bodpad/unicom24.test.git
cd unicom24.test
```
Устанавливаем виртуальное окружение и все необходимые для работы пакеты
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Запускаем сервер
```
python3 manage.py runserver
```

## Документация

### Аутентификация
Аутентификация пользователей реализована посредством токенов. Токен пользователя явно передается в строке url, а не http заголовком, для удобного тестирования GET запросов в браузере и просто так захотелось.

###
Версионность API не реализована преднамеренно.

### Выполнение запросов к API
Все запросы к API должны быть предсталены в такой форме:

    https://example.ru/api/U:<token>/METHOD_NAME/

где ***METHOD_NAME*** один из двух методов: ***customerProfile*** или ***request2CreditOrganization***

### Группы пользователей
Разграничение прав доступа для пользователей организовано с помощью стандартного механизма Django groups.
Каждый пользователь системы ***ДОЛЖЕН*** состоять в одной из трех групп: Суперпользователи, Партнеры или Кредитные организации.
Любой запрос пользователя к API, не состоящего ни в одной из трех групп, будет возвращать "403 Forbidden"

### Тестовые пользователи
Т. к. условием тестового задания продиктовано создание 3-х типов пользователей с разграниченными правами, ниже предствален список тестовых пользователей, которыми можно совершать запросы к API.

| Логин | Пароль | Токен | Группа |
| ----- | ------ | ----- | ------ |
| demouser1 | Demo1234 | 6da5e20491ef64596571be46069dc41c00b0d2bb | Суперпользователи (superuser) |
| demouser2 | Demo1234 | 7974b74525131c43a2e610da7a31e880e746b0be | Партнеры (partner) |
| demouser3 | Demo1234 | 0bfb13f818456199dc29a6c4f01b953123bd8115 | Кредитные организации (credit_organization) |

Так же имеется суперюзер имеющий доступ к админке:
```
Логин: admin
Пароль: Demo1234
```

### Немного тестирования
    Группа "Партнеры"
    # Получение списка анкет клиентов. Должен вернуть - 200 OK
    http GET http://127.0.0.1:8000/api/U:7974b74525131c43a2e610da7a31e880e746b0be/customerProfile/
    # Просмотр анкеты по ID. Должен вернуть - 200 OK
    http GET http://127.0.0.1:8000/api/U:7974b74525131c43a2e610da7a31e880e746b0be/customerProfile/1/
    # Cоздание анкеты. Должен вернуть - 201 Created
    http POST http://127.0.0.1:8000/api/U:7974b74525131c43a2e610da7a31e880e746b0be/customerProfile/ 'surname=Иванов' 'name=Иван' 'patronymic=Иванович' 'credit_score=300' 'phone_number=9881234567' 'passport_no=1234555555' 'birth_date=1993-02-01'
    # Редактирование анкеты по ID. Должен вернуть - 403 Forbidden
    http PUT http://127.0.0.1:8000/api/U:cf96d51ff38cf1b29f46475f6ef73e55cb4f73db/customerProfile/1/ 'surname=ААА'
    # Удаление анкеты по ID. Должен вернуть - 403 Forbidden
    http DELETE http://127.0.0.1:8000/api/U:7974b74525131c43a2e610da7a31e880e746b0be/customerProfile/1/
    # Отправка заявки в кредитные организации. Должен вернуть - 201 Created
    http POST http://127.0.0.1:8000/api/U:7974b74525131c43a2e610da7a31e880e746b0be/request2CreditOrganization/ 'customer_profile=1' 'offer=1'
    
    #-> Остальные запросы будут возвращать 403 Forbidden
    
    Группа "Кредитные организации"
    # Получение списка заявок. Должен вернуть - 200 OK
    http http://127.0.0.1:8000/api/U:0bfb13f818456199dc29a6c4f01b953123bd8115/request2CreditOrganization/
    # Просмотр заявки по ID. Должен вернуть - 200 OK
    http http://127.0.0.1:8000/api/U:0bfb13f818456199dc29a6c4f01b953123bd8115/request2CreditOrganization/1/
    
    #-> Остальные запросы будут возвращать 403 Forbidden
    
***
