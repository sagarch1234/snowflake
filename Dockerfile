FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update &&\
    apt-get install python3-dev default-libmysqlclient-dev gcc  -y &&\
    apt-get install -y libssl-dev libffi-dev &&\
    python -m pip install --upgrade pip &&\
    mkdir /snowflake-backend

WORKDIR /snowflake-backend

COPY ./requirements.txt /requirements.txt

COPY . /snowflake-backend

EXPOSE 80

ENV DATABASE_NAME=dropoff_development_database
ENV DATABASE_USERNAME=dropoff
ENV DATABASE_PASSWORD=dropoff@123
ENV DATABASE_HOST=34.71.45.17
ENV DATABASE_PORT=3306

ENV EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
ENV EMAIL_HOST=smtp.office365.com
ENV EMAIL_PORT=587
ENV EMAIL_USE_TLS=True

ENV EMAIL_HOST_USER=SnowflakeOptimizer@emphasistech.net
ENV EMAIL_HOST_PASSWORD=Sn0wFl@k3

RUN pip install -r /requirements.txt

RUN pip install -U "celery[redis]"

RUN python manage.py makemigrations &&\
    python manage.py migrate

RUN python manage.py loaddata usergroup account_type

CMD [ "python", "manage.py", "runserver", "0.0.0.0:80"]