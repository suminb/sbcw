# Homework 4

일반적으로 내부 함수는 직접 호출 할 수 없다. 내부 함수들이 다음과 같이 정의되어있을 때 글로벌 스코프에서 first_child() 와 second_child() 를 호출할 수 있도록 만들어라.

```python
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child
```

```
>>> first_child()
Hi, I am Emma
```
