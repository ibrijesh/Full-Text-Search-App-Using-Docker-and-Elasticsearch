FROM nginx:1.21.1

WORKDIR /etc/nginx/sites-enabled/

RUN rm -f default

COPY default  /etc/nginx/sites-enabled/default


RUN nginx


CMD ["nginx", "-g", "daemon off;"]