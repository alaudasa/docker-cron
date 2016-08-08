## Use the docker images

This is a example Dockerfile
```
FROM index.alauda.cn/alaudasa/docker-cron

# place you cron job file under /cron
ADD /path/to/your_cron_file /cron/your_cron_file
```

## place your cron file in /cron
the cron file under /cron will be move to /etc/cron.d directory when docker run, below is a example cron file:
```
* * * * * root echo "hello" > /logs/hello.log 2>&1
```

## cron job's log volume: /cronlogs
Cron job's log will not write to stdout and stderr. If you want to log, you have to write log to a mounted volume.Docker image define a volume /cronlogs to store the log. For example you run a Docker container:

```
docker run -d -v /local/cron/logs:/cronlogs/ my-docker-cron
```
