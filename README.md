В данном проекте реализована проверка CRUD операций в тестовом API https://restful-booker.herokuapp.com/apidoc/index.html с использованием библиотеки Requests

:radio_button: Создание "бронирования" на сайте

:radio_button: Проверка "бронирования"

:radio_button: Редактирование созданного

:radio_button: Проверка успешного редактирования

:radio_button: Удаление "бронирования"

:radio_button: Проверка удаления

Для запуска тестов локально необходимо в командной строке прописать:
        pip install -r requirements.txt
        pytest .
              
---

В данном сервисе запрос к endpoint проходит с использованием автосгенерированного токена. Получение токена в тестах реализовано в файле conftest.py осредством фикстуры get_token,которая передается в качетсве параметра в тестовых функциях.

Кроме того, для операций PUT и DELETE необходим id созданной сущности,который также генерируется автоматически при каждом запросе на создание сущности. В данном варианте реализации тестов полученный id записывается в файл id.txt и считывается из данного файла при следующих операциях.
            

---

 ### Запуск в Jenkins : [JOB](https://jenkins.autotests.cloud/job/RESTFUL_BOOKING%20API%20TESTS/)
 
 Нажать на кнопку Собрать сейчас
![Альтернативный текст](https://github.com/andrechizh8/api_tests_restful/blob/main/readme%20files/restful1.png)

После сборки есть возможность посмотреть отчет с различными приложениями: 

Скриншот:

![Альтернативный текст](https://github.com/andrechizh8/api_tests_restful/blob/main/readme%20files/restful2.png)


Кроме того, в проекте реализована возможность просмотр отчета в  Allure TestOps : 

![Альтернативный текст](https://github.com/andrechizh8/api_tests_restful/blob/main/readme%20files/restful3.png)

И интеграция с Jira :

![Альтернативный текст](https://github.com/andrechizh8/api_tests_restful/blob/main/readme%20files/restful4.png)

После прохождения тестов с использованием Jenkins в телеграмм приходит оповещение с результатами :

![Альтернативный текст](https://github.com/andrechizh8/api_tests_restful/blob/main/readme%20files/restful_telegramm.png)
