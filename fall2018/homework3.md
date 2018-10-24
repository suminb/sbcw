# Homework 3

이번 과제는 [이미 만들어진 파이썬 프로젝트][transporter]에서 각자 한 가지 이상의 기능을 구현해 보는 것이 목표이다.

## Problem 1

본격적으로 작업을 진행하기 전에 추가적인 환경 설정이 필요하다.

### Setting Up Docker

도커(Docker)를 설치해야 한다. 이미 설치 되어있다면 바로 다음 단계로 넘어간다.

- https://docs.docker.com/docker-for-mac/install/
- https://docs.docker.com/docker-for-windows/install/

명령창에서 `docker ps` 혹은 `docker images` 명령어를 수행했을 때 오류 메시지가 나오지 않고 (예를 들면 파일 권한 문제 등) 빈 리스트가 나오는 상태로 만들면 된다.

    (transporter) ➜  transporter git:(develop) ✗ docker images
    REPOSITORY            TAG           IMAGE ID         CREATED          SIZE

### Redis Server

[Transporter 프로젝트][transporter]는 효율적이고 빠른 데이터 캐싱을 위해 Redis를 사용한다. Redis 서버는 다음과 같이 실행할 수 있다.

    docker run -d -p 6379:6379 -p 6380:6380 redis:5.0

`redis:5.0` 이미지가 로컬 시스템에 존재하지 않으면 자동으로 원격 저장소에서 받아오도록 되어있다. 만약 도커가 자동으로 이미지를 받아오지 않는다면 다음 명령어를 실행해서 받아오도록 한다.

    docker pull redis:5.0

### PostgreSQL

데이터베이스 서버가 재시작 될 때마다 데이터가 초기화 되면 효율적으로 작업하기 어려울 수 있기 때문에 영속적인 저장소를 사용하도록 한다. 도커로 실행되는 PostgreSQL 서버의 데이터 디렉토리를 호스트 머신의 디렉토리에 매핑(mapping)함으로써 해결한다. 매핑을 하기 위해서 홈 디렉토리에 `postgres` 디렉토리를 만들어야 한다.

    docker run -d \
        -p 5432:5432 \
        -e POSTGRES_USER=postgres \
        -e POSTGRES_PASSWORD=qwerasdf \
        -e POSTGRES_DB=transporter \
        -v $HOME/postgres:/var/lib/postgresql/data \
        -t postgres:9.6

### 확인

PostgreSQL 서버에는 `psql` 명령어를 이용해서 접속할 수 있다. 다른 PostgreSQL 클라이언트를 사용해도 무방하다.

```
➜  ~ psql -h localhost -U postgres
Password for user postgres:
psql (10.5, server 9.6.10)
Type "help" for help.

postgres=#
```

위와 같이 `postgres:///postgres@localhost`에 접속할 수 있다면 정상이다.

Redis 는 별도의 클라이언트를 준비하여 접속하거나 다음과 같이 Telnet 으로 접속할 수 있다. `localhost:6379`에 접속해서 `PING` 명령어를 날려보고 응답으로 `PONG` 메시지가 돌아오면 정상이다.

```
(transporter) ➜  transporter git:(develop) ✗ telnet localhost 6379
Trying ::1...
Connected to localhost.
Escape character is '^]'.
PING
+PONG
```


[transporter]: https://github.com/suminb/transporter