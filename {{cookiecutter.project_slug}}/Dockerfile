FROM python:3.8-alpine as builder

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev openssl-dev build-base py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib

WORKDIR /build

# Requirements are installed here to ensure they will be cached.
COPY . .
RUN pip3 install pipenv
RUN pipenv lock --requirements > /build/requirements.txt

FROM python:3.8-alpine as app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev openssl-dev build-base py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib

# install dependencies
RUN pip install --upgrade pip

WORKDIR /app

COPY --from=builder /build/requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

COPY . .

RUN chmod +x /app/entrypoint
RUN chmod +x /app/migrator

ENTRYPOINT ["/app/entrypoint"]
