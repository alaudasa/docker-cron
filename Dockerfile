FROM ubuntu:14.04

RUN apt-get update && apt-get install -y python-minimal
COPY run-cron.py  /run-cron.py

VOLUME /cronlogs

CMD ["python", "/run-cron.py"]