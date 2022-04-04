FROM python:3.9

LABEL maintainer="devops@onix-systems.com"

ARG DEBIAN_FRONTEND=noninteractive
ARG GUNICORN_COUNT_WORKERS=4
ARG GUNICORN_COUNT_THREADS=4

ENV PYTHONBUFFERED = 1 \
    BIND_PORT=8000 \
    GUNICORN_COUNT_WORKERS=${GUNICORN_COUNT_WORKERS} \
    GUNICORN_COUNT_THREADS=${GUNICORN_COUNT_THREADS}

COPY ./docker-entrypoint.sh /

RUN apt-get update && \
    apt install -y \
    gettext-base \
    netcat \
    supervisor \
    nginx && \
    # clean apt
    apt-get autoremove && \
    apt-get autoclean && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /var/tmp/* && \
    chmod 755 /docker-entrypoint.sh

WORKDIR /var/www/app

COPY ./project_50/requirements.txt .

RUN python -m pip install --upgrade pip && pip install -r requirements.txt && pip install gevent

COPY ./.docker/nginx/web.conf /etc/nginx/sites-available/default
COPY ./.docker/supervisord /root/supervisord

COPY ./project_50 .

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 80