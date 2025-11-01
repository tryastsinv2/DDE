# Используем официальный Python образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock* ./

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Настраиваем Poetry для установки зависимостей в системный Python
RUN poetry config virtualenvs.create false

# Устанавливаем зависимости проекта
RUN poetry install --no-dev --no-interaction --no-ansi

# Копируем исходный код проекта
COPY . .

# Команда для запуска приложения
CMD ["python", "main.py"]