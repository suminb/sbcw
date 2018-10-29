# Homework 0

원활한 워크샵 진행을 위해 환경 설정을 미리 해 오는 것이 이번 숙제의 목표이다. 준비가 되지 않으면 진행이 어려울 수 있다.

## Problem 1: Python

파이썬 3.7 버전을 권장하지만, 3.6도 괜찮다.

    $ python --version
    Python 3.7.0

파이썬 인터프리터가 준비 되었다면 파이썬 패키지 관리자인 `pip`를 준비하도록 한다.

    $ pip --version
    pip 18.0 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)

참고할만한 문서: https://pip.pypa.io/en/stable/installing/

`pip`가 준비 되었다면 파이썬 가상 환경과 관리를 위한 패키지를 설치한다.

    pip install virtualenv

마지막으로, `virtualenv`를 조금 더 쉽게 사용할 수 있도록 패키징 해놓은 `virtualenvwrapper`를 설치한다.

    pip install virtualenvwrapper

안타깝게도 위 명령어만으로는 설치가 완벽하게 마무리 되지 않는다. 가상환경 디렉토리와 환경변수 설정 등을 직접 해주어야 합니다. [이 문서](https://virtualenvwrapper.readthedocs.io/en/latest/)를 참고하여 설치를 깔끔하게 마무리하도록 한다.

## Problem 2: Docker

도커를 설치한다.

    $ docker --version
    Docker version 18.06.1-ce, build e68fc7a

## Got Issues?

`#python_seminar` 채널에 물어보자.