FROM alpine:3.6

LABEL maintainer="insovoid@gmail.com"

RUN apk --no-cache add --virtual build-deps \
    ca-certificates \
    build-base \
    gfortran \
    cmake \
    && apk --no-cache add \
    python3 \
    python3-dev \
    lapack-dev \
    boost-dev \
    zlib-dev \
    libjpeg-turbo-dev \
    && update-ca-certificates \
    && pip3 install gunicorn flask face_recognition \
    && mkdir /app \
    && apk del build-deps

ADD main.py /app/
WORKDIR /app
ENTRYPOINT ["gunicorn", "main:app", "-w 2", "-b 0.0.0.0:80"]
