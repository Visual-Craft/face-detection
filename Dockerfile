FROM python:3.6

LABEL maintainer="insovoid@gmail.com"

RUN DEBIAN_FRONTEND=noninteractive apt update -y \
    && DEBIAN_FRONTEND=noninteractive apt upgrade -y \
    && DEBIAN_FRONTEND=noninteractive apt install --no-install-recommends -y \
        cmake \
    && pip install gunicorn flask face_recognition \
    && mkdir /app \
    && rm -rf /var/lib/apt

ADD main.py /app/
WORKDIR /app
ENTRYPOINT ["gunicorn", "main:app", "-b 0.0.0.0:80"]
CMD ["-w 2"]
