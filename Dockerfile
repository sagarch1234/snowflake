FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update &&\
    apt-get install python3-dev default-libmysqlclient-dev gcc  -y &&\
    mkdir /snowflake-backend

WORKDIR /snowflake-backend

COPY ./requirements.txt /requirements.txt

COPY . /snowflake-backend

EXPOSE 80

RUN pip install -r /requirements.txt

RUN python manage.py makemigrations &&\
    python manage.py migrate

# RUN python manage.py loaddata roles businesses route_status route_type order_status service_city payment_status

    
CMD [ "python", "manage.py", "runserver", "0.0.0.0:80"]