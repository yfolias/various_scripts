FROM ubuntu:latest
MAINTAINER Yannis Folias "yannis.folias@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential net-tools
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

