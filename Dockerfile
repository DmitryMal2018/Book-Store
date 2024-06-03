# Извлекаем базовый образ из официального образа Python
FROM python:3.10.4-slim-bullseye
# Отключает автоматическую проверку обновлений pip
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
# Python не будет создавать файлы *.pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Отключает буферизацию стандартного вывода
ENV PYTHONUNBUFFERED 1
# Рабочая папка
WORKDIR /Book-Store
# Установка зависимостей
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# Куда копировать проект
COPY . .