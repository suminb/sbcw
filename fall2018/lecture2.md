# Lecture 2

이번 강의부터는 낭비되는 바이트로 인한 통신장비의 과부하를 방지하고 저장장치에 사용되는 반도체 사용량을 줄임으로써 탄소배출량(carbon footprint)을 저감하기 위해 [하십시오체](https://ko.dict.naver.com/detail.nhn?docid=44848960) 대신 [해체](https://ko.dict.naver.com/detail.nhn?docid=41959900)를 사용하기로 한다.

## EAFP

(NOTE: 수강생이 소프트웨어 엔지니어라서 이 이야기를 먼저 할 수 있다. 클래스를 모르는 비개발자를 대상으로 할 때에는 이 섹션을 뒤로 보내야 할 것 같다.)

Q. 세입자와 파이썬 프로그래머의 공통점?

Easier to ask for forgiveness (EAFP). 허락을 구하기보단 용서를 구하라.

### 허락을 구하는 코드 1

```python
if len(xs) > i:
    print(xs[i])
else:
    print('i is out of bound', file=sys.stderr)
```

### 용서를 구하는 코드 1

```python
try:
    print(xs[i])
except IndexError:
    print('i is out of bound', file=sys.stderr)
```

### 허락을 구하는 코드 2

```python
if isinstance(x, Duck):
    x.quack()
else:
    x.meow()
```

### 용서를 구하는 코드 2

```python
try:
    x.quack()
except AttributeError:
    x.neow()
```

### 허락을 구하는 코드 3

```python
if os.access(csv_file, os.R_OK):
    with open(csv_file) as fin:
        print(fin.read())
else:
    print('File could not be accessed', file=sys.stderr)
```

### 용서를 구하는 코드 3

```python
try:
    fin = open(csv_file)
except IOError:
    print('File could not be accessed', file=sys.stderr)
else:
    with fin:
        print(fin.read())
```

## Duck Typing

```python
cat = Cat()
```

`cat`은 고양이 유전자(`class Cat`)를 물려받아서 고양이인가, 아니면 고양이처럼 행동하기(`Cat.meow()`) 때문에 고양이인가?

## Classes

**클래스**란 무엇인가? 섣불리 한마디로 정의하려고 했다가는 여기저기 박제되어 온갖 욕을 얻어먹을 것이 불보듯 뻔하기 때문에 일단 [파이썬 공식 문서](https://docs.python.org/3/tutorial/classes.html)의 첫 문단을 인용하기로 한다.

> Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

더 자세하고 재미있는 이야기는 강의시간에 하도록 한다.

### Namesapce and Scope

(TODO: 설명 쓰기)

> Although scopes are determined statically, they are used dynamically. At any time during execution, there are at least three nested scopes whose namespaces are directly accessible:
> 
> * the innermost scope, which is searched first, contains the local names
> * the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
> * the next-to-last scope contains the current module’s global names
> * the outermost scope (searched last) is the namespace containing built-in names

> It is important to realize that scopes are determined textually: the global scope of a function defined in a module is that module’s namespace, no matter from where or by what alias the function is called. On the other hand, the actual search for names is done dynamically, at run time — however, the language definition is evolving towards static name resolution, at “compile” time, so don’t rely on dynamic name resolution! (In fact, local variables are already determined statically.)

> A special quirk of Python is that – if no global statement is in effect – assignments to names always go into the innermost scope. Assignments do not copy data — they just bind names to objects. The same is true for deletions: the statement del x removes the binding of x from the namespace referenced by the local scope.

* `global`
* `nonlocal`

```python
def scope_test():
    def do_local():
        spam = 'local spam'

    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'

    def do_global():
        global spam
        spam = 'global spam'

    spam = 'test spam'
    do_local()
    print('After local assignment:', spam)
    do_nonlocal()
    print('After nonlocal assignment:', spam)
    do_global()
    print('After global assignment:', spam)

scope_test()
print('In global scope:', spam)
```

https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces

### Class Definitions

클래스는 다음과 같이 정의할 수 있다.

```python
class Cat:
    pass
```

`if`, `try`/`except` 등 제어문 안쪽이나 함수 내부에 선언하는 것도 가능하다.

```python
try:
    from sbcw import Cat
except ImportError:
    class Cat:
        pass
```

함수와 마찬가지로 클래스가 정의될 때 클래스를 위한 네임스페이스가 생겨난다. 그리고 클래스를 정의하는 코드 블럭이 끝날 때 클래스 객체가 생성된다. 파이썬에서는 클래스도 객체다.

### Legacy Notes

사실, 파이썬에서 클래스를 정의하는 방법은 두 가지가 있다.

#### *Classic* Style

```python
class Cat:
    pass
```

#### *New* Style

```python
class Cat(object):
    pass
```

둘 간의 차이가 있는가?

- 요약하자면, Python 2.x 버전에서는 차이가 있지만, 3.x에서는 두 스타일이 완전히 동일한 결과를 만들어낸다.
- 더 자세한 내용은 [StackOverflow 페이지](https://stackoverflow.com/questions/4015417/python-class-inherits-object)를 참고.

#### Python 2.7

```
>>> class Cat:
...     pass
...
>>> Cat.__bases__
()
```

```
>>> class Cat(object):
...     pass
...
>>> Cat.__bases__
(<type 'object'>,)
```

#### Python 3.7

```
>>> class Cat:
...     pass
...
>>> Cat.__bases__
(<class 'object'>,)
```

```
>>> class Cat(object):
...     pass
...
>>> Cat.__bases__
(<class 'object'>,)
```

### Class Objects

(TODO: 내용 채워넣기)

### Methods

```python
class Cat(object):

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hi there! My name is {self.name}'

    def attack(self):
        raise NotImplemented
```

### 클래스의 비밀(?)

```python
tom = Cat('Tom')
tom.greet()
```

```python
tom = Cat('Tom')
Cat.greet(tom)
```

### Special Method for String Representation

```python
class Cat(object):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Cat-{hash(self):x} ({self.name})'
```

```
>>> cat = Cat('May')
>>> cat
Cat-106af147 (May)
```

### Special Methods for Iterator

```python
class Series(object):

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.current = lower_bound

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.upper_bound:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1  # C/C++처럼 `return self.current++` 표현을 사용할 수 있었다면...
```

### Special Methods for `with` Statement

```python
class Session(object):

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        pass

    def execute(self, query):
        pass
```

```python
s = Session()
with s:
    s.execute(query)
```

### More Special Methods

http://www.diveintopython3.net/special-method-names.html


### Inheritance

```python
class Amniota(Tetrapod):
    pass

class Mammal(Amniota):
    pass

class Cat(Mammal):
    pass
```

### Multiple Inheritance

<img src="https://i.ytimg.com/vi/jS4uoqlVL_c/maxresdefault.jpg">

```python
class Building(Unit):
    pass

class CommandCenter(Building, AirUnit):
    pass
```

### Private Variables

파이썬에는 언어 레벨에서 강제할 수 있는 private 변수가 없다. 컨벤션으로만 존재한다.

> “Private” instance variables that cannot be accessed except from inside an object don’t exist in Python. However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API.

## Metaclasses

```
>>> class Cat:
...   pass
...

>>> cat = Cat()

>>> type(cat)
<class '__main__.Cat'>

>>> type(Cat)
<class 'type'>

>>> type(type)
<class 'type'>
```

```python
Cat = type('Cat', (object,), {'name': 'Tom'})
```

```
>>> Cat.name
Tom
```

```python
class Meta(type):

    def __new__(cls, name, bases, attrs):
        return super().__new__(cls, name, bases, attrs)


class Cat(metaclass=Meta):

    def __init__(self, name):
        self.name = name
```

https://realpython.com/python-metaclasses/
