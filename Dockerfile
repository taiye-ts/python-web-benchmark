FROM python:3.8.1-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install --no-install-recommends --assume-yes \
        bash \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /app \
    && mkdir -p /python


COPY requirements.txt /python

WORKDIR /app
RUN pip install --upgrade pip==19.3.1 && pip install --no-cache-dir -r /python/requirements.txt

COPY start.sh /python
RUN chmod +x /python/start.sh
COPY src /app

ENV PYTHONPATH="/app:${PATH}"
