FROM python:3.7
WORKDIR /simple-flask-starter
COPY . .
RUN apt-get -y update
RUN pip3 install -r requirements.txt
CMD [ "python","./run.py"]

