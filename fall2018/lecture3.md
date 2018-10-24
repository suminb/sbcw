# Lecture 3

이번 시간의 목표는 간단한 파이썬 프로젝트를 직접 만들어 보는 것이다. 파이썬의 문법을 이해하는 것도 중요하지만, 실제로 파이썬으로 코딩을 하려고 하면 문법 이외의 부분에서 막히는 경우가 많다. 그 중 하나가 프로젝트 구성이다. 직접 간단한 프로젝트를 구성해봄으로써 프로젝트 디렉토리의 구조를 이해하고, 소프트웨어 프로젝트가 온전하게 작동하는데 필요한 구성 요소들(e.g., 패키지 의존성 관리, 테스트, CI 등)을 어떻게 배치하는지 체험해 보는 것이 주요 내용이다.

## Python Project Structure

- Requirements file (`requirements.txt`)
- README
- License
- Setup script (`setup.py`)
- Documentation
- Test suite
- Continuous integration (CI)

https://docs.python-guide.org/writing/structure/

### Requirements file

```
flask
flask==1.0.2
flask>=1.0.0
flask>=1.0.0,<=1.0.2
git+https://github.com/pallets/flask.git@master
```

```
pip install -r requirements.txt
```

#### `install_requires` vs Requirements Files

- `requirements.txt` 파일 대신 `setup.py`에 의존성을 명시할 수 있다.
- Semantic versioning
- 하지만 특정 버전으로 고정하는건 일반적으로 좋은 관습이 아니다.

https://packaging.python.org/discussions/install-requires-vs-requirements/

### Setup Script

#### `distutils` vs. `setuptools`

https://stackoverflow.com/questions/25337706/setuptools-vs-distutils-why-is-distutils-still-a-thing

#### `setup.py` 예제

```python
#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

import finance


def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except:
        return '(Could not read from README.rst)'


setup(
    name='finance',
    version=finance.__version__,
    description='Personal Finance Project',
    long_description=readme(),
    author=finance.__author__,
    author_email=finance.__email__,
    url='http://github.com/suminb/finance',
    license='BSD',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'finance = finance.__main__:cli'
        ]
    },
)
```

https://docs.python.org/2/distutils/setupscript.html

### Test Suite

파이썬에 기본으로 포함된 [`unittest`](https://docs.python.org/3/library/unittest.html) 패키지 대신 [`pytest`](https://docs.pytest.org)를 이용한다. `pytest`는 테스트 코드에서 파이썬의 `assert` 구문을 그대로 이용할 수 있고, 픽스쳐(fixture) 관련 고급 기능들을 제공하고, 쉽게 확장할 수 있는 등 여러가지 유용한 기능들을 제공한다.

- `tests` 디렉토리 안에 있는 `test_*.py` 파일들
- `test_` 로 시작하는 함수들

https://docs.pytest.org/en/latest/getting-started.html

### Continuous Integration (CI)

https://docs.travis-ci.com/user/getting-started/

## 간단한 웹 애플리케이션 만들어보기

댓글 서비스를 만들어보자. 기초적인 CRUD 작업을 지원하는 웹 애플리케이션이다.

- Flask
- SQLAlchemy