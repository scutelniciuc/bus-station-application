FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend
COPY . /backend/

RUN pip install -r requirements.txt

EXPOSE 8000
