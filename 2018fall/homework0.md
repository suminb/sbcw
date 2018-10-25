Prep Homework
=============

다음의 명령어가 실행될 수 있는 환경을 구축하세요. 맥 사용자라면 [Homebrew 를 이용하여 설치](https://docs.brew.sh/Homebrew-and-Python)할 수 있습니다. 윈도우 사용자라면 [Anaconda](https://www.anaconda.com/download/)를 사용하는 것이 편리할 수도 있습니다. 직접 설치해도 무방합니다.

```
$ python --version
Python 3.7.0
```

참고: `3.6`도 괜찮긴 하지만, `3.7`과 미묘하게 달라서 추가적으로 문제 해결을 할 일이 생길 수도 있습니다.

```
$ pip --version
pip 18.0 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)
```

`pip`는 [이 문서](https://pip.pypa.io/en/stable/installing/)를 참고해서 설치해주세요. 우분투 리눅스 사용자라면 `apt install python-pip` 명령어로 간편하게 설치할 수 있습니다.

`pip`를 설치했다면 파이썬 가상 환경 구성과 관리를 위한 패키지를 설치하도록 합니다. (Anaconda를 설치했다면 이 과정은 생략해도 좋습니다.)

```
pip install virtualenv
```

마지막으로, `virtualenv`를 조금 더 쉽게 사용할 수 있도록 패키징 해놓은 `virtualenvwrapper`를 설치합니다.

```
pip install virtualenvwrapper
```

안타깝게도 위 명령어만으로는 설치가 완벽하게 마무리 되지 않습니다. 가상환경 디렉토리와 환경변수 설정 등을 직접 해주어야 합니다. [이 문서](https://virtualenvwrapper.readthedocs.io/en/latest/)를 참고하여 설치를 깔끔하게 마무리하도록 합니다.
