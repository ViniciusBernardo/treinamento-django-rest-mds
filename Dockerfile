FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/treinamento/treinamento/tests_coverage
WORKDIR /home/treinamento/treinamento

ADD requirements.txt ..
RUN pip install -r ../requirements.txt
