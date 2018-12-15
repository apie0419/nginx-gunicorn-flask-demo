FROM python:3.6

COPY app/ /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
