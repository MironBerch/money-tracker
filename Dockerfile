FROM python:3.10-alpine

WORKDIR /app

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt  /app/requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]
