FROM python:3.9.10-buster

ADD . /scheduler
WORKDIR /scheduler

RUN pip install -r requirements.txt

CMD [ "python3", "-u", "scheduler.py" ]