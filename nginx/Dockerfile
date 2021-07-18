FROM ibrijesh/elasticsearch-flask-nginx

WORKDIR /etc/nginx/sites-enabled/

RUN rm -f /etc/nginx/sites-enabled/default

COPY default  /etc/nginx/sites-enabled/default


WORKDIR /usr/src/app/

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

# RUN export FLASK_APP=app.py
# RUN python3 -m flask run --host=0.0.0.0


# ENTRYPOINT ["nginx"]

CMD ["nginx","./entrypoint.sh"]