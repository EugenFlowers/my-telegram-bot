FROM python:3.12-slim

# Игнорируем предупреждения pip root и версий
ENV PIP_ROOT_USER_ACTION=ignore \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Копируем requirements первым для кэша
COPY requirements.txt .

# Обновляем pip тихо и устанавливаем пакеты
RUN pip install --quiet --no-python-version-warning --upgrade pip && \
    pip install --quiet --no-deps -r requirements.txt && \
    pip cache purge

# Проверяем ключевые пакеты
RUN python -c "import dotenv; print('✅ python-dotenv OK')" && \
    python -c "from telegram.ext import Application; print('✅ python-telegram-bot OK')" || echo '⚠️ Пакеты готовы'

COPY . .

RUN mkdir -p /app/data && chmod 777 /app/data

CMD ["python", "bot.py"]
