FROM python:3.6-slim

MAINTAINER varunkumar032@gmail.com

COPY . /python-test-calculator

WORKDIR /UITAP



RUN cd UITAP
RUN pip install --no-cache-dir -r requirements.txt

RUN ["pytest", "-v", "--junitxml=reports/result.xml"]

CMD tail -f /dev/null
