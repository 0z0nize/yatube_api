![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)
## Описание.

Проект «API для Yatube».

### **Технологии**
![python version](https://img.shields.io/badge/Python-3.9.10-yellowgreen?logo=python)
![django version](https://img.shields.io/badge/Django-3.2.16-yellowgreen?logo=django)
![djangorestframework version](https://img.shields.io/badge/djangorestframework-3.12.4-yellowgreen?logo=django)
![pytest version](https://img.shields.io/badge/pytest-6.2.4-yellowgreen?logo=pytest)
![requests version](https://img.shields.io/badge/requests-2.26.0-yellowgreen?logo=requests)

### Как запустить проект:

_Клонировать репозиторий и перейти в него в командной строке:_

```
git clone https://github.com/0z0nize/api_final_yatube.git
```

```
cd api_final_yatube
```

_Cоздать и активировать виртуальное окружение:_

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/Scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

_Установить зависимости из файла requirements.txt:_

```
pip install -r requirements.txt --use-pep517
```

_Выполнить миграции:_

```
python3 manage.py migrate
```

_Запустить проект:_

```
python3 manage.py runserver
```

_Документация к API проекта Yatube:_

```
http://127.0.0.1:8000/redoc/
```
_Примеры работы с API для неавторизованных пользователей пользователей:_

```
GET api/v1/posts/ - список публикаций
GET api/v1/posts/{id}/ - публикациия
GET api/v1/posts/?limit=100&offset=200 - список публикаций с пагинацией
```

```
GET api/v1/groups/ - список сообществ
GET api/v1/groups/{id}/ - описание сообщества по id
```
```
GET api/v1/{post_id}/comments/ - список комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - комментарий к публикации
```
