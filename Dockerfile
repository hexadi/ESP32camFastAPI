FROM python:3.8-slim-buster

RUN pip install fastapi uvicorn python-multipart aiofiles

RUN apt update && apt-get install nginx -y

COPY ./esp32 /etc/nginx/sites-available/esp32

RUN ln -s /etc/nginx/sites-available/esp32 /etc/nginx/sites-enabled/esp32

RUN rm /etc/nginx/sites-enabled/default

COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

COPY ./app /app

ADD start.sh /
RUN chmod +x /start.sh

CMD ["/start.sh"]