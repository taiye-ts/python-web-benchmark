# How to start

```shell script
brew install wrk
docker-compose build
```

## Selecting framework and db

In docker-compose there two env variables in backend service
DB = {mongo, mysql, postgres}
FRAMEWORK {flask, falcon}

## Starting test env
```shell script
docker-compose up <db> backend
```

## Running benchmark
```shell script
wrk -c 40 -t 2 -d 10s -s bench.lua --latency  http://127.0.0.1:8042/test
```
