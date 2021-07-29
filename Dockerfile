FROM python:latest

WORKDIR /server

COPY requirements.txt /server
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /server

RUN python3 manage.py makemigrations
RUN python3 manage.py makemigrations article
RUN python3 manage.py migrate 
