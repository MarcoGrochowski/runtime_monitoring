FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=".:/runtime_monitor"

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt