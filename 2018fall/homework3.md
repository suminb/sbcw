# Homework 3

이번 과제는 [이미 만들어진 파이썬 프로젝트][transporter]에서 각자 한 가지 이상의 기능을 구현해 보는 것이 목표이다.

## Problem 1

본격적으로 작업을 진행하기 전에 추가적인 환경 설정이 필요하다.

### Setting Up Docker

도커(Docker)를 설치해야 한다. 이미 설치 되어있다면 바로 다음 단계로 넘어간다.

- https://docs.docker.com/docker-for-mac/install/
- https://docs.docker.com/docker-for-windows/install/

명령창에서 `docker ps` 혹은 `docker images` 명령어를 수행했을 때 오류 메시지가 나오지 않고 (예를 들면 파일 권한 문제 등) 빈 리스트가 나오는 상태로 만들면 된다.

    ➜  transporter git:(develop) ✗ docker images
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
➜  transporter git:(develop) ✗ psql -h localhost -U postgres
Password for user postgres:
psql (10.5, server 9.6.10)
Type "help" for help.

postgres=#
```

위와 같이 `postgres:///postgres@localhost`에 접속할 수 있다면 정상이다.

Redis 는 별도의 클라이언트를 준비하여 접속하거나 다음과 같이 Telnet 으로 접속할 수 있다. `localhost:6379`에 접속해서 `PING` 명령어를 날려보고 응답으로 `PONG` 메시지가 돌아오면 정상이다.

```
➜  transporter git:(develop) ✗ telnet localhost 6379
Trying ::1...
Connected to localhost.
Escape character is '^]'.
PING
+PONG
```

## Problem 2

저번 시간에는 클래스에서 SQLite 에 데이터를 읽고 쓰는 것을 연습해보았는데, 이번에는 PostgreSQL 에 데이터를 읽고 쓰는 것을 연습해 보는 것이 목표이다. 사실, SQLAlchemy 같은 ORM 을 이용한다면 어떤 데이터베이스를 이용하든 코드 레벨에서 크게 달라질 것은 없다.

저번 워크샵 시간에 다같이 만들었던 간단한 CRUD 웹 앱 코드를 정리해서 [`webapp.py`](https://github.com/suminb/sbcw/blob/master/2018fall/webapp.py) 를 만들어두었다. 이 코드를 그대로 사용하는 것을 추천하지만, 저번 시간에 만들었던 코드에서 그대로 이어 나가도 괜찮다.

위 코드에서 의존하는 패키지는 다음과 같다.

- `flask`
- `flask-sqlalchemy`

코드를 보면 다음과 같이 데이터베이스 연결을 위한 URI를 명시하는 설정 변수가 있다.

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
```

이 부분을 변경해서 1번 문제에서 만든 PostgreSQL 서버에 접속할 수 있도록 만드는 것이 이 문제의 요구사항이다.

SQLite 와 마찬가지로 PostgreSQL 데이터베이스에서도 최초에 한 번 테이블을 생성해주어야 한다. SQLite 에서는 하나의 파일이 하나의 데이터베이스에 대응되는 방식이었지만, PostgreSQL 에는 여러개의 데이터베이스, 여러명의 유저가 동시에 호스팅 될 수 있기 때문에 데이터베이스도 생성해주어야 한다.

    psql -h localhost -U postgres -c "CREATE DATABASE webapp"

`webapp` 이라는 이름을 가진 데이터베이스를 생성했지만, 다른 이름으로 해도 무방하다. 그런 다음, 파이썬 REPL 을 띄워서 다음의 코드를 실행시키면 필요한 테이블이 생성된다.

```python
from webapp import app, db

with app.app_context():
    db.create_all()
```

마지막으로 `webapp`이 기존의 동작들을 잘 수행하는지 확인해본다.

- 포스트 만들기
- 포스트 읽어오기
- 포스트 업데이트
- 포스트 삭제

### 유용한 도구들

이 글에서는 PostgreSQL에 접속하기 위한 도구로 명령창 도구인 `psql`를 사용하지만, 명령창 사용이 익숙하지 않다면 GUI 도구를 이용해도 좋다.

- https://dbeaver.io/
- https://www.pgadmin.org/


`GET` 요청을 제외한 다른 형식의 요청들은 웹브라우저를 이용해서 테스트하기 쉽지 않기 때문에 다음의 도구 중 하나를 골라 사용하는 것을 권장한다.

- https://www.getpostman.com/
- https://curl.haxx.se/

웹브라우저 확장 기능도 있으니 참고하면 좋다. (직접 테스트 해보지는 못했다.)

- https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo
- https://addons.mozilla.org/en-US/firefox/addon/restclient/

[transporter]: https://github.com/suminb/transporter