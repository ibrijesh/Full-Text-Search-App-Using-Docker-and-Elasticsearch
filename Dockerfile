
FROM ubuntu:latest

RUN apt update

RUN apt upgrade -y

RUN apt install vim -y

# Install nginx 

RUN apt install nginx -y

#Install python3 and pip

RUN apt install python3 -y
RUN apt-get -y install python3-pip

#install elasticsearch , pandas and Flask

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt


# Remove defualt nginx setting and add your own setting

WORKDIR /etc/nginx/sites-enabled/

RUN rm -f /etc/nginx/sites-enabled/default

COPY nginx/default  /etc/nginx/sites-enabled/default


# copy the entrypoint script

RUN nginx

WORKDIR /usr/src/app


COPY ./esflask/ ./

RUN chmod +x entrypoint.sh

EXPOSE 5000

EXPOSE 80

CMD [ "./entrypoint.sh"]