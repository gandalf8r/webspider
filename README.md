1. Для встановлення залежностей:
- cd webscraper
- pip install -r requirements.txt

2. Для запуску docker-compose: якщо знаходимося в корні проекту 
- cd webscraper/postgres
- docker-compose up

3. Для виконання міграцій пишемо в консолі: якщо знаходимося в корні проекту
- cd webscraper
- python manage.py migrate

4. Для запуску додатка:
- python manage.py runserver

Додаткова інформація:
1. Для економії часу перевірки та збору даних проходимо по перших 4 сторінках
2. Для наглядності виводимо номер сторінки яка обробляється в консоль