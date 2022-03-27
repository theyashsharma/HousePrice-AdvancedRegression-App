FROM python:3.8.8

WORKDIR /HousePriceApp

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

