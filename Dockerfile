FROM python:latest

MAINTAINER "XAVIER TORRENT sendotux@gmail.com"

RUN apt-get update -y && apt-get install -y python3-pip python3-dev

RUN pip3 install flask

WORKDIR /app

COPY /app /app

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
