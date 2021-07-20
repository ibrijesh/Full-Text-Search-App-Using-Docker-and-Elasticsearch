FROM python:3.9.6


WORKDIR /app


ADD . /app

RUN pip3 install --no-cache-dir -r requirements.txt


RUN chmod +x entrypoint.sh


EXPOSE 5000


CMD ["./entrypoint.sh"]