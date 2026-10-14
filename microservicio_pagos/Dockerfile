FROM python:3.11-alpine

WORKDIR /app

RUN pip install --no-cache-dir flask gunicorn

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--access-logfile", "-", "--error-logfile", "-", "--bind", "0.0.0.0:5000", "app:app"]
