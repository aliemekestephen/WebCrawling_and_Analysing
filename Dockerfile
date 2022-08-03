FROM python:3.10
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pipenv install --no-cache-dir -r requirements.txt
COPY . /usr/src/app

CMD ["python", "./Utils/menu.py"]

