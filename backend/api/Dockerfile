# Dockerfile for FastAPI Webapp
FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install gunicorn

CMD gunicorn bot.webapp.app:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 --log-level debug
