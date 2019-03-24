FROM ubuntu:latest
MAINTAINER Your Name "yannis.folias@gmail.com"
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev build-essential net-tools

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]