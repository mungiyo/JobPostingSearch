FROM python:3.9.10-buster

ADD . /api
WORKDIR /api

RUN pip install -r requirements.txt

CMD [ "python3", "-u", "app.py" ]