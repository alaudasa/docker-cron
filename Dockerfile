FROM ubuntu:14.04

RUN apt-get update && apt-get install -y python-minimal
COPY test.sh /test.sh
COPY run-cron.py  /run-cron.py
COPY test.cron /cron/
RUN chmod a+x /test.sh

VOLUME /cronlogs

CMD ["python", "/run-cron.py"]