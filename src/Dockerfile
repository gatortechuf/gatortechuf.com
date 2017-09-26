FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY . .

CMD python manage.py collectstatic --noinput && \
    python manage.py makemigrations && \
    python manage.py migrate --fake-initial && \
    gunicorn gatortech.wsgi -b 0.0.0.0:8000
