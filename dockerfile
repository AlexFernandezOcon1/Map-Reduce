FROM python:3.8


WORKDIR /src
COPY TextCounter ./
COPY words.py ./
COPY WordCounter.py ./
COPY histograma.py ./
COPY TextCounter.py ./
COPY ArcTecSw_2022_BigData_Practica_Part1_Sample.txt ./

RUN chmod +x TextCounter


