FROM python:3.6-slim

MAINTAINER varunkumar032@gmail.com

COPY . /python-test-calculator

WORKDIR / 

RUN pip freeze > requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /UITAP

RUN ["pytest", "-v", "--junitxml=reports/result.xml"]

CMD tail -f /dev/null
