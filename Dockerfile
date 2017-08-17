FROM daocloud.io/nginx

ADD . /usr/share/nginx/html/

LABEL SERVICE_NAME=web@ent
