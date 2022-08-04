FROM python:3.10
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
# COPY App /usr/src/app
#COPY App/Credentials /usr/src/app
#COPY App/Locators /usr/src/app
#COPY App/Pages /usr/src/app
#COPY App/Parsers /usr/src/app
#COPY App/Utils /usr/src/app


RUN pip install --no-cache-dir -r requirements.txt # here is the last change

COPY . /usr/src/app

#RUN python -m venv / py && \
##    /py/bin/pip install --upgrade pip && \
#    pip install -r /requirement.txt && \
#    adduser --disabled-password --no-create-home app

CMD ["python", "./App/app.py"]



#ENV PATH="/py/bin:$PATH"
#USER app