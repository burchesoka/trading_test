FROM python:3.11

WORKDIR /trading

COPY ./requirements.txt /trading/requirements.txt

ADD .env .env
RUN export `cat .env`

RUN mkdir /trading/logs

RUN pip install -U pip \
    && pip install -r /trading/requirements.txt

COPY . /trading/
