## Установка и запуск проекта FrameWorkSdetTest

1. Склонировать репозиторий
```
https://github.com/Farkhat1986/FrameWorkSdetTest
```
2. Перейти в директорию проекта
3. Создать вируальное окружение
```
python -m venv venv
```
4. Активировать окружение
```
venv\Scripts\activate
```
5. Установка зависимостей
```
pip install -r requirements.txt
```
6. Запуск тестов и запись результатов 
```
pytest --alluredir=allure-results
```
7. Запуск отчета allure c результатами тестов
```
allure serve allure-results
```