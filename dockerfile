FROM python:3.8


WORKDIR /src
COPY TextCounter ./
COPY words.py ./
COPY WordCounter.py ./
COPY histograma.py ./
COPY TextCounter.py ./


RUN chmod +x TextCounter


