FROM python:3.10
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt # here is the last change
RUN apt-get update
RUN apt-get -y install apt-utils
RUN apt install -y python3-tk

#CMD export DISPLAY:0

COPY . /usr/src/app


CMD ["python", "./App/app.py"]
