FROM python:3.9

LABEL maintainer="devops@onix-systems.com"

ENV BIND_PORT=8000

# netcat is required for wait_for function
RUN apt-get update && \
  apt-get install -y \
  gettext-base \
  gdal-bin \
  libgdal-dev \
  python3-gdal \
  libproj-dev \
  netcat && \
  apt-get clean && \
  mkdir -p /var/www/api_project

WORKDIR /var/www/api_project
RUN python -m pip install --upgrade pip
COPY ./api_project/requirements.txt ./

RUN pip install -r requirements.txt && \
  pip install gevent

COPY ./api_project /var/www/api_project
# COPY ./api_project/admin_panel/static /var/www/api_project/admin_panel/static_2
COPY ./docker-entrypoint.sh /
RUN chmod 755 /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]