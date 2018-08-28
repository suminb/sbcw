## Problem 1

친구들에게 단체 이메일을 보내려고 하는데, 이메일 주소 전체가 아닌 유저 이름 부분만 담긴 텍스트 파일이 주어졌습니다.

    alejandro, britney, christina, dennis, emily

유저 이름 뒤에 `@gmail.com`을 붙여야 하는데, 이걸 수동으로 하기에 우리 인생은 너무 짧습니다. 이것을 다음과 같이 변환하는 코드를 작성하십시오.

    alejandro@gmail.com
    britney@gmail.com
    christina@gmail.com
    dennis@gmail.com
    emily@gmail.com

여러분이 할 일은 `homework1.py`에 있는 `convert()` 함수를 구현하는 것입니다. `text`가 주어졌을 때 세미콜론(`;`)으로 구분된 이메일 주소들을 반환하는 함수입니다. 이 함수가 반환한 문자열을 이메일 주소 칸에 그대로 붙여넣으면 단체 메일을 보낼 수 있습니다.

    def convert(text):
        # 여기에 여러분의 코드를 작성하세요
        pass

## 자동 채점

코드를 테스트 하기 위해서는 `pytest` 패키지가 필요합니다. 다음의 명령어를 실행하여 설치하도록 합니다.

    pip install pytest

패키지가 설치되면 다음과 같이 테스트 파일을 실행해서 여러분이 작성한 코드가 제대로 작동되는지 검증하도록 합니다.

    pytest -v test_homework1.py

## 참고할만한 자료

- https://www.datacamp.com/community/tutorials/data-structures-python
