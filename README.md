# Yatube API

API для социальной сети Yatube - платформы для публикации постов, комментариев и подписок на авторов.

## Описание

Yatube API предоставляет REST API для взаимодействия с социальной сетью. Пользователи могут:

- Создавать, просматривать, редактировать и удалять посты
- Добавлять и просматривать комментарии к постам
- Подписываться на других пользователей
- Просматривать группы и фильтровать посты по группам
- Управлять своим контентом через JWT-аутентификацию

## Технологии

- Python 3.11+
- Django 3.2.16
- Django REST Framework 3.12.4
- JWT-аутентификация (djangorestframework-simplejwt)
- Djoser для управления пользователями
- SQLite (по умолчанию)
- uv для управления зависимостями

## Установка

### Предварительные требования

Убедитесь, что у вас установлен [uv](https://docs.astral.sh/uv/getting-started/installation/):

```bash
# macOS и Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Или через pip
pip install uv
```

### Настройка проекта

1. Клонируйте репозиторий:
```bash
git clone <url-репозитория>
cd api_final_yatube
```

2. Установите зависимости и создайте виртуальное окружение:
```bash
uv sync
```

3. Активируйте виртуальное окружение:
```bash
# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate

# Или используйте uv run для выполнения команд без активации
```

4. Выполните миграции:
```bash
uv run python yatube_api/manage.py makemigrations
uv run python yatube_api/manage.py migrate
```

5. Создайте суперпользователя (опционально):
```bash
uv run python yatube_api/manage.py createsuperuser
```

6. Запустите сервер:
```bash
uv run python yatube_api/manage.py runserver
```

API будет доступно по адресу: http://127.0.0.1:8000/api/v1/

## Управление зависимостями

### Добавление новых зависимостей
```bash
# Добавить зависимость
uv add package-name

# Добавить зависимость для разработки
uv add --dev package-name

# Добавить конкретную версию
uv add "package-name==1.0.0"
```

### Обновление зависимостей
```bash
# Обновить все зависимости
uv sync --upgrade

# Обновить конкретную зависимость
uv add package-name --upgrade
```

### Удаление зависимостей
```bash
uv remove package-name
```

## Запуск тестов

```bash
# Запуск всех тестов
uv run pytest

# Запуск конкретного теста
uv run pytest tests/test_specific.py

# Запуск с покрытием
uv run pytest --cov
```

## Аутентификация

Для получения JWT-токена отправьте POST-запрос на `/api/v1/jwt/create/` с данными пользователя:

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

В ответ вы получите access и refresh токены. Используйте access токен в заголовке Authorization:

```
Authorization: Bearer your_access_token
```

## Примеры запросов к API

### Получение списка постов
```http
GET /api/v1/posts/
```

### Создание нового поста (требуется аутентификация)
```http
POST /api/v1/posts/
Content-Type: application/json
Authorization: Bearer your_access_token

{
    "text": "Текст поста",
    "group": 1
}
```

### Получение комментариев к посту
```http
GET /api/v1/posts/1/comments/
```

### Добавление комментария (требуется аутентификация)
```http
POST /api/v1/posts/1/comments/
Content-Type: application/json
Authorization: Bearer your_access_token

{
    "text": "Текст комментария"
}
```

### Получение списка групп
```http
GET /api/v1/groups/
```

### Получение подписок (требуется аутентификация)
```http
GET /api/v1/follow/
Authorization: Bearer your_access_token
```

### Подписка на пользователя (требуется аутентификация)
```http
POST /api/v1/follow/
Content-Type: application/json
Authorization: Bearer your_access_token

{
    "following": "username_to_follow"
}
```

### Поиск по подпискам (требуется аутентификация)
```http
GET /api/v1/follow/?search=username
Authorization: Bearer your_access_token
```

## Документация API

Полная документация API доступна по адресу: http://127.0.0.1:8000/redoc/

## Права доступа

- **Неаутентифицированные пользователи**: только чтение постов, комментариев и групп
- **Аутентифицированные пользователи**:
  - Создание постов и комментариев
  - Редактирование и удаление своего контента
  - Управление подписками
- **Подписки**: доступны только аутентифицированным пользователям

## Разработка

### Структура проекта
```
api_final_yatube/
├── yatube_api/          # Django приложение
├── tests/               # Тесты
├── pyproject.toml       # Конфигурация проекта и зависимости
├── uv.lock              # Файл блокировки зависимостей
└── README.md            # Этот файл
```

### Полезные команды

```bash
# Показать информацию о проекте
uv show

# Показать дерево зависимостей
uv tree

# Проверить устаревшие зависимости
uv sync --upgrade-package package-name

# Запуск команды в виртуальном окружении
uv run <command>

# Создать новое виртуальное окружение
uv venv

# Активировать shell с виртуальным окружением
uv shell
```
