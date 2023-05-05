![233348780-313ad8af-8fa5-47e0-8f1c-7f0aea8c24a122](https://user-images.githubusercontent.com/112638163/234629394-ba57d889-a76c-4842-abe5-067a2d3301de.png)

### Описание.
CRUD для Yatube
* В проекте api_yatube есть приложение posts с описанием моделей Yatube. В нём реализовано API для всех моделей приложения.
* Вся логика API вынесена в отдельное приложение. 
* API доступен только аутентифицированным пользователям. Используется аутентификация по токену TokenAuthentication.
* Аутентифицированный пользователь авторизован на изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.
* При попытке изменить чужие данные возвращается код ответа 403 Forbidden.

### Технологии.
![python version](https://img.shields.io/badge/Python-3.9.10-yellowgreen?logo=python)
![django version](https://img.shields.io/badge/Django-3.2.16-yellowgreen?logo=django)
![djangorestframework version](https://img.shields.io/badge/djangorestframework-3.12.4-yellowgreen?logo=django)
![pytest version](https://img.shields.io/badge/pytest-6.2.4-yellowgreen?logo=pytest)
![requests version](https://img.shields.io/badge/requests-2.26.0-yellowgreen)

### Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/0z0nize/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

- Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

- Если у вас windows

    ```
    source env/Scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt --use-pep517
```

Выполнить миграции:

```
python3 manage.py migrate
```

_Запустить проект:_

```
python3 manage.py runserver
```

Документация к API проекта Yatube:

```
http://127.0.0.1:8000/redoc/
```
Примеры работы с API для неавторизованных пользователей пользователей:

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

### Автор проекта:
#### [_Владислав Шкаровский_](https://github.com/0z0nize)
