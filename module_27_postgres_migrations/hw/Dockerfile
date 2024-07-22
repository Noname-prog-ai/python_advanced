FROM python:3.11-slim

# Установим зависимости
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Запуск приложения с помощью Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]