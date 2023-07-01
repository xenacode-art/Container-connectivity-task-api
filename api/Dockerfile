FROM python:alpine3.15
WORKDIR /app
ADD requirements.txt models.py api.py ./
RUN apk update --no-cache \
  && apk add gcc g++ musl-dev mariadb-connector-c-dev mysql-client \
  && pip3 install -r requirements.txt
CMD ["python3", "/app/api.py"]