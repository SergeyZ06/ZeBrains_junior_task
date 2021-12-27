**Задание:**

2. Разработать Веб-сервис image-text-recognition на базе любого OCR фреймворка.
- Для создания REST API можно использовать что удобно, FastApi, Flask, Django и т. п..
- В качестве фреймворка можно использовать любой, например easyocr, mmocr, keras-ocr и тому подобные.
- Достаточно одного REST эндпоинта POST /text-recognition на вход которого подаётся картинка, на выходе получаем распознанный текст.
- Описать решение в README.md.
- Код запушить в GitHub и предоставить ссылку.
- Нужно будет объяснить, как работает сервис и выбранная модель.

**Решение:**

Здравствуйте.

Для решения задачи визуального разбора текста был использован фреймворк EasyOCR,
для реализации REST API - фреймворк Flask.

Веб-сервис принимает POST запрос с изображением, затем в битовом представлении
передаёт в функцию ocr(). В данной функции с помощью EasyOCR производится разбор текста,
который Flask возвращает на запрос.

Также был реализован модуль "test_request.py" для проверки работоспособности сервиса.
