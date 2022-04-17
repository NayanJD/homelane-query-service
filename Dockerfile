FROM python:3.9.10

ENV APP_HOME=/src

WORKDIR /src

ADD . .

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "-b", "0.0.0.0"]