FROM python:3.12-slim

ENV PIP_ROOT_USER_ACTION=ignore \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --quiet --upgrade pip && \
    pip install --quiet -r requirements.txt && \
    pip cache purge

COPY . .
RUN mkdir -p /app/data && chmod 777 /app/data

CMD ["python", "bot.py"]
