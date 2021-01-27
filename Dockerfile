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

#DATABASE STAGING ENV
ENV DATABASE_NAME=snowflake_staging
ENV DATABASE_USERNAME=staging_admin
ENV DATABASE_PASSWORD=so@root_123
ENV DATABASE_HOST=so-staging-db.postgres.database.azure.com
ENV DATABASE_PORT=5432
ENV SECRET_KEY=*g1qx7cs&9g)-x6_!%9#65eafzfx$ush%+t!v&=!y3z)q#=x27

#EMAIL STAGING ENV
ENV EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
ENV EMAIL_HOST=smtp.office365.com
ENV EMAIL_PORT=587
ENV EMAIL_USE_TLS=True
ENV EMAIL_HOST_USER=SnowflakeOptimizer@emphasistech.net
ENV EMAIL_HOST_PASSWORD=Sn0wFl@k3

#AZURE STAGING ENV
ENV AZURE_ACCOUNT_NAME=sostagingstore
ENV AZURE_ACCOUNT_KEY=M9F+gOlsYmcIsje5O+J+ajlv0M2KAsua9vm2VAymyl4QlETFdtW2AeYISk1rzQ1110jv0eISIf/lXcj+nJP0tg==>
ENV AZURE_LOCATION=sostagingcontainer
ENV AZURE_CONTAINER=sostagingcontainer

#SNOWFLAKE SFO's STAGING ENV
ENV SNOWFLAKE_ACCOUNT_USER=SFOPT_TEST_APP
ENV SNOWFLAKE_ACCOUNT_PASSWORD=(sE&Gv]82qv^3KJU
ENV SNOWFLAKE_ACCOUNT=ya78377.east-us-2.azure
ENV SNOWFLAKE_DATABASE_NAME=SFOPT_TEST
ENV SCHEMA_NAME_PARAMS=PARAMS
ENV SCHEMA_NAME_AUDITS=AUDITS
ENV ACCOUNT_ROLE=SFO_TEST_APP_ROLE
ENV ACCOUNT_WAREHOUSE=SFOPT_TEST_WH

RUN pip install -r /requirements.txt

RUN pip install -U "celery[redis]"
RUN pip install snowflake-connector-python[pandas]


# RUN python manage.py makemigrations &&\
#     python manage.py migrate

# RUN python manage.py loaddata usergroup account_type audit_status

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:80"]